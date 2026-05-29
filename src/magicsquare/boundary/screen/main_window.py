"""Main window — submit grid to boundary orchestrator and show results."""

from __future__ import annotations

from typing import Any

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from magicsquare.boundary.dto import ValidationFailureResult
from magicsquare.boundary.orchestrator import process_grid_submission
from magicsquare.boundary.presenter import (
    format_solver_pending,
    format_validation_failure,
)
from magicsquare.boundary.screen.grid_io import GridCellParseError, read_grid_from_cell_texts
from magicsquare.boundary.screen.grid_panel import GridPanel


class _GuiSolverPort:
    """Stub port for GUI; ``resolve`` is not invoked until solve path is GREEN."""

    def resolve(self, grid: Any) -> Any:
        """Placeholder — domain solver not wired."""
        raise NotImplementedError("Domain solver not implemented")


class MainWindow(QMainWindow):
    """Magic Square 4×4 input and boundary validation feedback."""

    def __init__(self) -> None:
        """Assemble grid, actions, and status area."""
        super().__init__()
        self.setWindowTitle("Magic Square XX — 4×4")
        self.setMinimumSize(360, 420)
        self._solver_port = _GuiSolverPort()
        self._grid_override: list[list[int]] | None = None
        self._grid = GridPanel(self)
        self._connect_grid_edit_signals()
        self._status = QLabel(self)
        self._status.setWordWrap(True)
        self._status.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft,
        )
        self._status.setText(
            "Enter values 0–16 (empty = 0). Submit runs size validation."
        )
        submit_btn = QPushButton("Submit", self)
        submit_btn.clicked.connect(self._on_submit)
        clear_btn = QPushButton("Clear", self)
        clear_btn.clicked.connect(self._on_clear)
        demo_btn = QPushButton("Demo: 3 rows × 4 cols", self)
        demo_btn.clicked.connect(self._on_demo_bv_04a)
        demo_btn_b = QPushButton("Demo: 4 rows × 3 cols", self)
        demo_btn_b.clicked.connect(self._on_demo_bv_04b)
        sample_btn = QPushButton("Load sample 4×4", self)
        sample_btn.clicked.connect(self._on_load_sample)
        button_row = QHBoxLayout()
        button_row.addWidget(submit_btn)
        button_row.addWidget(clear_btn)
        button_row.addWidget(demo_btn)
        button_row.addWidget(demo_btn_b)
        button_row.addWidget(sample_btn)
        button_row.addStretch()
        title = QLabel("4×4 Magic Square Grid", self)
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        central = QWidget(self)
        layout = QVBoxLayout(central)
        layout.addWidget(title)
        layout.addWidget(self._grid, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(button_row)
        layout.addWidget(QLabel("Result:", self))
        layout.addWidget(self._status)
        self.setCentralWidget(central)

    def _connect_grid_edit_signals(self) -> None:
        self._grid.connect_cell_edited(self._clear_grid_override)

    def _clear_grid_override(self) -> None:
        self._grid_override = None

    def _on_clear(self) -> None:
        self._grid_override = None
        self._grid.clear_grid()
        self._set_status_info("Grid cleared.")

    def _on_load_sample(self) -> None:
        """Fill a complete 4×4 grid for size-valid submit demo."""
        self._grid_override = None
        self._grid.set_all_cells_active()
        self._grid.set_grid_texts(
            [
                ["16", "3", "2", "13"],
                ["5", "10", "11", "8"],
                ["9", "6", "7", "12"],
                ["4", "15", "14", "1"],
            ]
        )
        self._set_status_info("Sample 4×4 loaded — Submit checks size (solver pending).")

    def _run_invalid_size_demo(
        self,
        grid: list[list[int]],
        label: str,
    ) -> None:
        """Submit a non-4×4 grid and show INVALID_SIZE with dimension label."""
        result = process_grid_submission(
            grid=grid,
            solver_port=self._solver_port,
        )
        if isinstance(result, ValidationFailureResult):
            message = format_validation_failure(result)
            self._set_status_error(f"{label} → {message}")
        else:
            self._set_status_success(f"Unexpected: {result!r}")

    def _on_demo_bv_04a(self) -> None:
        """BV-04a: 3 rows × 4 columns (UT-01 / G-04)."""
        from magicsquare.boundary.screen.demo_grids import GRID_BV_04A_3_ROWS_4_COLS

        self._grid.show_bv_04a_preview()
        self._grid_override = [row[:] for row in GRID_BV_04A_3_ROWS_4_COLS]
        self._run_invalid_size_demo(
            self._grid_override,
            "BV-04a (3 rows × 4 cols)",
        )

    def _on_demo_bv_04b(self) -> None:
        """BV-04b: 4 rows × 3 columns (G-05)."""
        from magicsquare.boundary.screen.demo_grids import GRID_BV_04B_4_ROWS_3_COLS

        self._grid.show_bv_04b_preview()
        self._grid_override = [row[:] for row in GRID_BV_04B_4_ROWS_3_COLS]
        self._run_invalid_size_demo(
            self._grid_override,
            "BV-04b (4 rows × 3 cols)",
        )

    def _on_submit(self) -> None:
        if self._grid_override is not None:
            grid = self._grid_override
        else:
            try:
                grid = read_grid_from_cell_texts(self._grid.cell_texts())
            except GridCellParseError as exc:
                self._set_status_error(
                    f"Cell ({exc.row},{exc.col}): use empty or 0–16.",
                )
                return
            except ValueError as exc:
                self._set_status_error(str(exc))
                return
        try:
            result = process_grid_submission(
                grid=grid,
                solver_port=self._solver_port,
            )
        except NotImplementedError:
            self._set_status_info(format_solver_pending())
            return
        if isinstance(result, ValidationFailureResult):
            self._set_status_error(format_validation_failure(result))
            return
        self._set_status_success(f"Success: {result!r}")

    def _set_status_error(self, message: str) -> None:
        self._status.setStyleSheet("color: #b00020; font-weight: bold;")
        self._status.setText(message)

    def _set_status_info(self, message: str) -> None:
        self._status.setStyleSheet("color: #333333;")
        self._status.setText(message)

    def _set_status_success(self, message: str) -> None:
        self._status.setStyleSheet("color: #00695c; font-weight: bold;")
        self._status.setText(message)

    def closeEvent(self, event: Any) -> None:
        """Confirm exit when grid has unsaved edits (non-empty cells)."""
        texts = self._grid.cell_texts()
        has_data = any(text.strip() for row in texts for text in row)
        if has_data:
            answer = QMessageBox.question(
                self,
                "Quit",
                "Discard grid input and quit?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            if answer != QMessageBox.StandardButton.Yes:
                event.ignore()
                return
        event.accept()
