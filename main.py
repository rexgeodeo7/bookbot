from stats import get_words, get_characters, sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

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

    for item in sorted_dict:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()