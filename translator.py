from googletrans import Translator

x = input("Choose a language: ").lower()
lang_list = {"german": "de", "french": "fr", "italian": "it", "bosnian": "ba", "serbian": "sr", "croatian": "hr"}
y = lang_list[x]

def translator(word):
    translator = Translator()
    translation = translator.translate(word, src='en', dest=y) 
    return translation.text

word_to_translate = input("Name an English word so it can be translated into the selected language: ")
translating = translator(word_to_translate)
print(f"{word_to_translate} in that language is {translating}")
