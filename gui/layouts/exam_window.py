"""

Layout for ExamWindow

"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout


def exam_layout(window):
    window.btn_layout = QHBoxLayout()
    window.btn_layout.addWidget(window.btn_back)
    window.btn_layout.addWidget(window.btn_next)

    window.layout = QVBoxLayout()
    window.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
    window.layout.addWidget(window.label_time)
    window.layout.addWidget(window.question)
    window.layout.addWidget(window.answer)
    window.layout.addLayout(window.btn_layout)

    return window.layout
