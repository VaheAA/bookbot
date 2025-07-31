from stats import count_words, count_characters, show_report
import sys

def get_book_text(path):
    with open(path, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")

    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    char_counter = count_characters(book_text)

    sorted_chars = show_report(char_counter)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        if not item['char'].isalpha:
            continue
        else:
            print(f"{item["char"]}: {item["num"]}")

main()
