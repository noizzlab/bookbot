from stats import *
import sys



def main():
    book_path = get_args()
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_list = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list_orig(characters_list)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_args():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    else:
        return sys.argv[1]
    sys.exit(1)

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
