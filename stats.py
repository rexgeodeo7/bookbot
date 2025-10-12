def get_words(text):
    words_count = 0
    words = text.split()

    for word in words:
        words_count += 1

    return words_count

def get_characters(text):
    characters = {}

    for letter in text:
        lower_letter = letter.lower()

        if lower_letter not in characters:
            characters[lower_letter] = 1
        
        else:
            characters[lower_letter] += 1

    return characters