"""PyQt6 application entry for Magic Square XX."""

from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication

from magicsquare.boundary.screen.main_window import MainWindow


def main() -> int:
    """Launch the Magic Square GUI.

    Returns:
        Process exit code from ``QApplication.exec()``.
    """
    app = QApplication(sys.argv)
    app.setApplicationName("Magic Square XX")
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
