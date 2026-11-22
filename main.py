import sys
from pathlib import Path

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from AboutWindow import AboutWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ice Cream Sales")
        self.resize(1000, 700)
        self.setMinimumSize(720, 520)

        self.temperatures = []
        self.revenues = []
        self.about_window = None

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(28, 24, 28, 28)
        main_layout.setSpacing(18)

        header_layout = QHBoxLayout()
        title_layout = QVBoxLayout()
        title = QLabel("Ice Cream Sales")
        title.setObjectName("pageTitle")
        subtitle = QLabel("Explore the relationship between temperature and revenue")
        subtitle.setObjectName("pageSubtitle")
        title_layout.addWidget(title)
        title_layout.addWidget(subtitle)
        header_layout.addLayout(title_layout)
        header_layout.addStretch()

        self.load_button = QPushButton("Load File")
        self.load_button.setObjectName("primaryButton")
        self.load_button.clicked.connect(self.load_file)
        header_layout.addWidget(self.load_button)

        self.about_button = QPushButton("About")
        self.about_button.setObjectName("secondaryButton")
        self.about_button.clicked.connect(self.show_about)
        header_layout.addWidget(self.about_button)
        main_layout.addLayout(header_layout)

        chart_container = QWidget()
        chart_container.setObjectName("chartCard")
        chart_layout = QVBoxLayout(chart_container)
        chart_layout.setContentsMargins(16, 16, 16, 16)
        chart_layout.setSpacing(8)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, chart_container)
        chart_layout.addWidget(self.toolbar)
        chart_layout.addWidget(self.canvas, stretch=1)
        main_layout.addWidget(chart_container, stretch=1)

        self.draw_graph()

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select a CSV file",
            "",
            "CSV files (*.csv)",
        )
        if file_path:
            # TODO: Read the CSV into self.temperatures and self.revenues.
            self.draw_graph()

    def draw_graph(self):
        self.figure.clear()
        axes = self.figure.add_subplot(111)
        axes.plot([18, 22, 26, 30, 34], [12, 19, 27, 38, 52], marker="o")
        axes.set_title("Sample temperature vs. revenue")
        axes.set_xlabel("Temperature")
        axes.set_ylabel("Revenue")
        axes.grid(True, linestyle="--", alpha=0.35)
        self.figure.tight_layout()
        self.canvas.draw()

    def show_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()


def main():
    app = QApplication(sys.argv)
    stylesheet_path = Path(__file__).with_name("style.qss")
    app.setStyleSheet(stylesheet_path.read_text(encoding="utf-8"))

    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())