"""

Grid-Layout for Window Training with translation

"""
# imports
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout


def training_eng_layout(window):
    german = QVBoxLayout()
    german.addWidget(window.question)
    german.addWidget(window.explanation)
    german.setAlignment(Qt.AlignmentFlag.AlignLeft)
    german.setContentsMargins(10, 10, 10, 10)

    english = QVBoxLayout()
    english.addWidget(window.question_e)
    english.addWidget(window.explanation_e)
    english.setAlignment(Qt.AlignmentFlag.AlignRight)
    english.setContentsMargins(10, 10, 10, 10)

    question = QHBoxLayout()
    question.addLayout(german)
    question.addLayout(english)
    question.setAlignment(Qt.AlignmentFlag.AlignCenter)

    btn_layout = QHBoxLayout()
    btn_layout.addWidget(window.btn_show)
    btn_layout.addWidget(window.btn_next)
    btn_layout.setAlignment(Qt.AlignmentFlag.AlignRight)

    layout = QVBoxLayout()
    layout.addLayout(question)
    layout.addLayout(btn_layout)

    return layout
