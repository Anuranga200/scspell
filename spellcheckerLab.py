from spellchecker import SpellChecker

spell = SpellChecker()

# Sample text with errors
text = "Ths is a smple paragraf with spleling erors."

# Split the text into words and check each one
words = text.split()
misspelled = spell.unknown(words)

for word in misspelled:
    # Get the most likely correct spelling
    correct_word = spell.correction(word)
    print(f"{word} -> {correct_word}")
