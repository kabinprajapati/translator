from googletrans import Translator


def translate(text):
    translator = Translator()
    translation = translator.translate(text=text, dest='ne')
    return translation.text
