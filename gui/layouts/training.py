"""

Grid-Layout for Window Training

"""
# imports
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout


def training_layout(window):
    qu_layout = QVBoxLayout()
    qu_layout.addWidget(window.question)
    qu_layout.addWidget(window.explanation)
    qu_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    btn_layout = QHBoxLayout()
    btn_layout.addWidget(window.btn_show)
    btn_layout.addWidget(window.btn_next)
    btn_layout.setAlignment(Qt.AlignmentFlag.AlignRight)

    qu_layout.addLayout(btn_layout)

    return qu_layout
