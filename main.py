from stats import get_num_words, get_letter_count, sort_letters
import sys 

def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        doc = get_book_test(book)
        letter_count = get_letter_count(doc)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}")
        print("----------- Word Count -----------")
        print(f"Found {get_num_words(doc)} total words")
        print("------------ Character Count ------")
        sort_letters(letter_count)
        print("============== END ==============")

main()