import pyttsx3

FILENAME = ".speech"

engine = pyttsx3.init()


def generate(text):
    engine.save_to_file(text, FILENAME)
    engine.runAndWait()
    return FILENAME
