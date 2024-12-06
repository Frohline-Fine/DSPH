"""

Grid-Layout für Window Main

"""
# imports
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout


def main_layout(window):
    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(window.btn_training)
    layout.addWidget(window.btn_training_e)
    layout.addWidget(window.btn_exam)
    layout.addWidget(window.btn_exit)

    return layout
