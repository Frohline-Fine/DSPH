"""

Layout for audit results

"""

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout


def audit_result_layout(window):
    header_layout = QHBoxLayout()
    header_layout.addWidget(window.correct_count)
    header_layout.addWidget(window.accuracy)

    layout = QVBoxLayout()
    layout.addLayout(header_layout)
    layout.addWidget(window.table)

    return layout
