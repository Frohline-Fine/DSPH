"""

Translate text into english

"""

import time
from googletrans import Translator


def translate(text):
    translator = Translator()
    translation = translator.translate(text, dest="en")
    # wait to bypass limitation
    time.sleep(1)
    return translation.text
