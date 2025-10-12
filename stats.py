def get_words(text):
    words_count = 0
    words = text.split()

    for word in words:
        words_count += 1

    return words_count