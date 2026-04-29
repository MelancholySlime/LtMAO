from PySide6.QtWidgets import QSplashScreen, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from . import helper

app = None

def build_splash():
    # build splash screen
    app.splash = splash = QSplashScreen()
    splash.setWindowFlags(splash.windowFlags()|Qt.WindowStaysOnTopHint)
    # splash background
    pixmap = QPixmap(app.theme_paths['splash']).scaled(400, 400, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
    splash.setPixmap(pixmap)
    # splash label
    label = QLabel()
    label.setStyleSheet('background-color: rgba(0, 0, 0, 127); color: rgba(255, 255, 255, 255);')
    helper.link_splash(label)
    # splash layout
    layout = QVBoxLayout()
    layout.addWidget(label, stretch=1, alignment=Qt.AlignmentFlag.AlignBottom)
    splash.setLayout(layout)
    
    print('qtGUI: Finish: Build splash screen.')