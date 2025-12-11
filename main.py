def get_book_text ():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents
def main ():
    text = get_book_text()
    print(text)
main()
