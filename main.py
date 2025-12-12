from stats import split_text,char_count, sort_count
import sys
def get_book_text (book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main ():
    print(len(sys.argv))
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("===========BOOKBOT===========")
    book = sys.argv[1]

    print(f"Analyzing book found at {book}")
    print("-------- Word Count ---------")
    text = get_book_text(book)
    print(f"Found {split_text(text)} total words")
    print("------ Character Count -------")
    letters = char_count(text)
    sorted_chars = sort_count(letters)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")


main()
