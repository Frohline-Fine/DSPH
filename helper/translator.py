"""
Translate text into english
"""
import time
import random
from googletrans import Translator

# generate a random delay between 1 and 5 seconds to bypass limitation
delay = random.randint(1, 3)


def translate(text):
    translator = Translator()
    translation = translator.translate(text, dest="en")
    time.sleep(delay)
    return translation.text
