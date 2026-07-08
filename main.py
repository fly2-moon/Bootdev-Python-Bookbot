import sys
from stats import open_book, get_num_words, count_characters, chars_dict_to_sorted_list

def print_report(book_path, word_count, count_list) -> None:
   print(
           "============ BOOKBOT ============\n"
           f"Analyzing book found at {book_path}...\n"
           "----------- Word Count ----------\n"
           f"Found {word_count} total words\n"
           "--------- Character Count -------"
           )
    
   for count_tuple in count_list:
        key:chr = count_tuple[1]
        value:int = count_tuple[0]
        print(f"{key}: {value}")

   print("============= END ===============")

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path:str = sys.argv[1]
    contents:str = open_book(book_path)
    word_count:int = get_num_words(contents)
    count_dict:dict = count_characters(contents)
    count_list = chars_dict_to_sorted_list(count_dict)

    print_report(book_path, word_count, count_list)
    
if __name__ == "__main__":
    main()

