from stats import get_words, get_characters

def main():
    book_path = "books/frankenstein.txt"

    # get text (string) to be used by the methods
    text = get_book_text(book_path)
    
    characters_dict = get_characters(text)

    words = get_words(text)

    print(characters_dict)
    print(f"Found {words} total words")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()