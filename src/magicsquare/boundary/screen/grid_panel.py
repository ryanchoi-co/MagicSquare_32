"""4×4 grid input panel (PyQt6)."""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QLineEdit, QSizePolicy, QWidget

_GRID_DIMENSION = 4
_INACTIVE_STYLE = "background-color: #ececec; color: #888888;"
_ACTIVE_STYLE = ""


def _int_grid_to_texts(grid: list[list[int]]) -> list[list[str]]:
    return [[str(value) for value in row] for row in grid]


class GridPanel(QWidget):
    """Editable 4×4 grid; empty cells represent 0."""

    def __init__(self, parent: QWidget | None = None) -> None:
        """Build a labeled 4×4 matrix of line edits."""
        super().__init__(parent)
        self._cells: list[list[QLineEdit]] = []
        layout = QGridLayout(self)
        layout.setSpacing(6)
        for row in range(_GRID_DIMENSION):
            row_cells: list[QLineEdit] = []
            for col in range(_GRID_DIMENSION):
                cell = QLineEdit(self)
                cell.setMaxLength(2)
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cell.setPlaceholderText("0")
                cell.setSizePolicy(
                    QSizePolicy.Policy.Fixed,
                    QSizePolicy.Policy.Fixed,
                )
                cell.setFixedWidth(48)
                layout.addWidget(cell, row, col)
                row_cells.append(cell)
            self._cells.append(row_cells)

    def cell_texts(self) -> list[list[str]]:
        """Return raw text for each cell row-major."""
        return [[cell.text() for cell in row] for row in self._cells]

    def clear_grid(self) -> None:
        """Clear all cell values and restore active styling."""
        self.set_all_cells_active()
        for row in self._cells:
            for cell in row:
                cell.clear()

    def set_all_cells_active(self) -> None:
        """Enable every cell and remove inactive highlight."""
        for row in self._cells:
            for cell in row:
                cell.setEnabled(True)
                cell.setStyleSheet(_ACTIVE_STYLE)
                cell.setPlaceholderText("0")

    def show_bv_04a_preview(self) -> None:
        """Show BV-04a: 3 rows × 4 cols; disable row 4 (not submitted as 4×4)."""
        from magicsquare.boundary.screen.demo_grids import GRID_BV_04A_3_ROWS_4_COLS

        self.set_all_cells_active()
        self.clear_grid()
        texts = _int_grid_to_texts(GRID_BV_04A_3_ROWS_4_COLS)
        for row_idx, row in enumerate(texts):
            for col_idx, text in enumerate(row):
                self._cells[row_idx][col_idx].setText(text)
        for cell in self._cells[3]:
            cell.clear()
            cell.setEnabled(False)
            cell.setStyleSheet(_INACTIVE_STYLE)
            cell.setPlaceholderText("—")

    def show_bv_04b_preview(self) -> None:
        """Show BV-04b: 4 rows × 3 cols; disable column 4 in each row."""
        from magicsquare.boundary.screen.demo_grids import GRID_BV_04B_4_ROWS_3_COLS

        self.set_all_cells_active()
        self.clear_grid()
        texts = _int_grid_to_texts(GRID_BV_04B_4_ROWS_3_COLS)
        for row_idx, row in enumerate(texts):
            for col_idx, text in enumerate(row):
                self._cells[row_idx][col_idx].setText(text)
        for row in self._cells:
            cell = row[3]
            cell.clear()
            cell.setEnabled(False)
            cell.setStyleSheet(_INACTIVE_STYLE)
            cell.setPlaceholderText("—")

    def connect_cell_edited(self, callback: object) -> None:
        """Wire ``textChanged`` on every cell to ``callback``."""
        for row in self._cells:
            for cell in row:
                cell.textChanged.connect(callback)  # type: ignore[arg-type]

    def set_grid_texts(self, values: list[list[str]]) -> None:
        """Fill cells from string values (must be 4×4)."""
        if len(values) != _GRID_DIMENSION:
            raise ValueError("Grid must have exactly 4 rows.")
        for row_idx, row in enumerate(values):
            if len(row) != _GRID_DIMENSION:
                raise ValueError("Each row must have exactly 4 columns.")
            for col_idx, text in enumerate(row):
                self._cells[row_idx][col_idx].setText(text)
