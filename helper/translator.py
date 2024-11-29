"""
Translates text into english
"""
from googletrans import Translator


def translate(text):
    translator = Translator()
    translation = translator.translate(text, dest="en")
    return translation.text
