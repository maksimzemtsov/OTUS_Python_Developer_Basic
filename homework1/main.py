import os
from book_actions import save, update_item, remove_item, show_all_items, add_item, find_item
from open_txt_book import open_txt_book

def main_menu():
    options_func = {
        'Open book': lambda: book_choose_menu(),
        'Exit': lambda: close_program()
    }
    menu_text, options_dict = get_menu_text_n_options(get_keys_list_from_dict(options_func))
    choice = get_choice(menu_text, len(options_dict))

    options_func[options_dict[choice]]()

def book_choose_menu():
    # Get books files
    options_func = {
        'Back': lambda: main_menu(),
        'Exit': lambda: close_program()
    }
    common_options = get_keys_list_from_dict(options_func)
    books_list = list(filter(lambda x: x.split('.')[-1] == 'txt', os.listdir('./phone_books')))
    options_list = books_list + common_options

    menu_text, options_dict = get_menu_text_n_options(options_list)

    choice = get_choice(menu_text, len(options_dict))

    if (choosen_option := options_dict[choice]) in common_options:
        options_func[choosen_option]()
    else:
        book_content = open_txt_book(choosen_option)
        if book_content:
            book_actions_menu(choosen_option, book_content)
        else:
            print('Invalid phone book file')
            book_choose_menu()

def book_actions_menu(file_name, book_content):
    options_func = {
        'Show all': lambda: show_all_items(book_content),
        'Find': lambda: find_item(book_content),
        'Remove': lambda: remove_item(book_content),
        'Add': lambda: add_item(book_content),
        'Update': lambda: update_item(book_content),
        'Save': lambda: save(book_content, file_name),
        'Back': lambda : book_choose_menu(),
        'Exit': lambda: close_program()
    }

    menu_text, options_dict = get_menu_text_n_options(get_keys_list_from_dict(options_func))

    while True:
        choice = get_choice(menu_text, len(options_dict))
        options_func[options_dict[choice]]()

def get_menu_text(options_dict: dict) -> str:
    """Return example: '1. Open book \n 2. Exit'"""
    return str.join('\n', [str.join('. ', item) for item in options_dict.items()])  + '\n: '

def get_menu_options(options_list: list) -> dict[str: str]:
    """Return example: {'1': 'Open book', '2': 'Exit'}"""
    return {str(i + 1): options_list[i] for i in range(len(options_list))}

def get_menu_text_n_options(options_list: list) -> tuple[str, dict]:
    """Return example: tuple('1. Open book \n 2. Exit', {'1': 'Open book', '2': 'Exit'})"""
    options_dict = get_menu_options(options_list)
    menu_text = get_menu_text(options_dict)

    return menu_text, options_dict

def get_choice(menu_text, options_count):
    warning_message = f'Choose correct option between 1 and {options_count}'
    while True:
        try:
            choice = input(menu_text)
            if not 0 < int(choice) <= options_count:
                raise ValueError
            return choice
        except ValueError:
            print(warning_message)

def close_program():
    raise SystemExit()

def get_keys_list_from_dict(dictionary: dict):
    return [item for item in dictionary.keys()]

if __name__ == "__main__":
    main_menu()