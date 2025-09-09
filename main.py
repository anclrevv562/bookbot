import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words, get_char_count, sort_on, sort_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    words = get_num_words(get_book_text(sys.argv[1]))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    chars = get_char_count(get_book_text(sys.argv[1]))
    sorted_chars = sort_dict(chars)
    for char in sorted_chars:
        if char.isalpha():
            print(f"{char}: {sorted_chars[char]}")
    print("============= END ===============")
    
main()
