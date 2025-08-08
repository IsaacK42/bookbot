import sys
from stats import get_num_words, get_char_counts, sort_characters_by_frequency

def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)

    word_count = get_num_words(book_text)
    char_counts = get_char_counts(book_text)
    sorted_characters = sort_characters_by_frequency(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...\n")
    print("--------- Word Count ---------")
    print(f"Found {word_count} total words\n")
    print("-------- Character Count -------")
    
    for entry in sorted_characters:
        print(f"{entry['char']}: {entry['num']}")
    
    print("============= END =============")

main()