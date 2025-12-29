import sys

from stats import count_words
from stats import count_letters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    
    print("============ BOOKBOT ============")
    print("")
    print(f"Analyzing book found at {book_path}...")
    print("")
    print("----------- Word Count ----------")
    print("")
    print(f"Found {word_count} total words")
    print("")
    print("--------- Character Count -------")
    print("")
    for letter, count in letter_count.items():
        print(f"  {letter}: {count}")
    print("")
    print("============= END ===============")
main()