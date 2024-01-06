import sys

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    book_word_count = get_word_count(book_text)
    chars = get_char_count_dict(book_text)

    print(f'--- Begin report of {book_path} ---\n')
    print(f'{book_word_count} total words in the book\n')

    chars_list = list(chars.items())
    chars_list.sort()
    
    for k, v in chars_list:
        if k.isalpha():
            print(f"The character '{k}' appears {v} times")
    
    print('--- End of report ---')


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def get_word_count(text):
    word_count = text.split()
    return len(word_count)


def get_char_count_dict(text):
    char_count = {}
    
    for char in text:
        lowered = char.lower()

        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1

    return char_count


if __name__ == '__main__':
    sys.exit(main())