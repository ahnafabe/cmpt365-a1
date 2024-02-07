import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TIFF Image Viewer")
        self.setGeometry(100, 100, 400, 400)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 300, 300)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.open_button = QPushButton("Open Image", self)
        self.open_button.setGeometry(20, 10, 120, 30)
        self.open_button.clicked.connect(self.open_image)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setGeometry(260, 10, 120, 30)
        self.exit_button.clicked.connect(self.close)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Image files (*.tif)")
        if file_path:
            image = QImage(file_path)
            pixmap = QPixmap.fromImage(image)
            scaled_pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label.setPixmap(scaled_pixmap)
            self.label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec_())
