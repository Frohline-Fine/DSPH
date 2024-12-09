"""

Layout for ExamWindow

"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout


def exam_layout(self=None):
    btn_layout = QHBoxLayout()
    btn_layout.addWidget(self.btn_back)
    btn_layout.addWidget(self.btn_next)

    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignmentFlag.AlignTop)
    layout.addWidget(self.label_time)
    layout.addWidget(self.question)
    layout.addWidget(self.answer)
    layout.addLayout(btn_layout)

    return layout
