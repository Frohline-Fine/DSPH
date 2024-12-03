"""
Grid-Layout für TrainingWindow
"""
# imports
from PyQt6.QtWidgets import QGridLayout


def training_layout(window):
    main_layout = QGridLayout()
    main_layout.setSpacing(20)
    main_layout.setContentsMargins(20, 20, 20, 20)

    main_layout.addWidget(window.label_question, 0, 0)
    main_layout.addWidget(window.label_question_e, 0, 1)

    main_layout.addWidget(window.label_answer, 1, 0)
    main_layout.addWidget(window.label_explanation, 2, 0)
    main_layout.addWidget(window.label_explanation_e, 2, 1)
    main_layout.addWidget(window.button_answer, 3, 0)
    main_layout.addWidget(window.button_reset, 3, 1)

    return main_layout
