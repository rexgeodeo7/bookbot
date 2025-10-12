from stats import get_words, get_characters, sort_dict

def main():
    book_path = "books/frankenstein.txt"

    # get text (string) to be used by the methods
    text = get_book_text(book_path)
    
    # make the char->value dict and then sort it
    characters_dict = get_characters(text)
    sorted_dict = sort_dict(characters_dict)

    # word count
    words = get_words(text)

    # print() structure
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    print(sorted_dict)
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()