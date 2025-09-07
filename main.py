from stats import get_num_words, character_occurrences, sort_characters
import sys

def get_book_text():
    with open(sys.argv[1], "r") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text()
    word_count = get_num_words(text)
    char_counts = character_occurrences(text)
    sorted_chars = sort_characters(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_data in sorted_chars:
        print(f"{char_data['char']}: {char_data['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()