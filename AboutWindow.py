from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
import sys

class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('אודות המפתח')
        self.setGeometry(200, 200, 400, 500)
        
        self.setStyleSheet("background-color: #f4f6f9;")

        self.my_picture = QLabel(self)
        self.my_picture.setGeometry(100, 30, 200, 200)
        image = QPixmap('monkey.webp').scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.my_picture.setPixmap(image)
        self.my_picture.setStyleSheet("border: 3px solid #2c3e50; border-radius: 10px;")

        self.my_name = QLabel('כפיר גלס', self)
        self.my_name.setGeometry(50, 250, 300, 40)
        self.my_name.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
       
        self.my_name.setAlignment(Qt.AlignCenter)

        self.my_desc = QLabel('סטודנט שנה ג׳ להנדסת מכונות, אפקה', self)
        self.my_desc.setGeometry(50, 290, 300, 30)
        self.my_desc.setStyleSheet("font-size: 15px; color: #7f8c8d;")
        self.my_desc.setAlignment(Qt.AlignCenter)

        self.my_email = QLabel('אימייל: kfirglass14@gmail.com', self)
        self.my_email.setGeometry(50, 340, 300, 30)
        self.my_email.setStyleSheet("font-size: 16px; color: #34495e;")
        self.my_email.setAlignment(Qt.AlignCenter)

        linkedin_html = '<a href="https://www.linkedin.com/in/kfir-glass-85b479434/" style="color: #2980b9; text-decoration: none;">לפרופיל הלינקדאין שלי</a>'
        self.my_linkedin = QLabel(linkedin_html, self)
        self.my_linkedin.setGeometry(50, 380, 300, 30)
        self.my_linkedin.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.my_linkedin.setAlignment(Qt.AlignCenter)
        self.my_linkedin.setOpenExternalLinks(True)

        github_html = '<a href="https://github.com/kfirglass?tab=repositories" style="color: #2980b9; text-decoration: none;">למאגר הקוד ב-GitHub</a>'
        self.my_github = QLabel(github_html, self)
        self.my_github.setGeometry(50, 420, 300, 30)
        self.my_github.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.my_github.setAlignment(Qt.AlignCenter)
        self.my_github.setOpenExternalLinks(True)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AboutWindow()
    window.show()
    app.exec()