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

def sort_helper(item):
    return item["num"]


def sort_dict(characters_dict):
    char_num_dict_list = []

    # breaks the dict of char->value into two dicts of char->char and value->count inside a list (2 dicts per index)
    for key in characters_dict:
        char_num_dict_list.append({"char": key, "num":characters_dict[key]})
    
    # sorts the list from highest to lowest
    char_num_dict_list.sort(reverse=True, key=sort_helper)
    return char_num_dict_list
