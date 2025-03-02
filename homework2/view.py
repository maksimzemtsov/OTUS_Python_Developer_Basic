from pathlib import Path
from model import Contact
import os


class PhoneBookManagerInterface:
    @staticmethod
    def show_welcome_menu():
        print(
            'Welcome to the Phone Book Manager!\n'
            '\n'
            '1. Go to the phone books list\n'
            '2. Exit\n'
        )

    @staticmethod
    def show_books_list(files: list[Path]) -> list[str]:
        menu_options = [*files, 'Back', 'Exit']
        output_string = '\n'.join([f'{i + 1}. {menu_options[i]}' for i in range(len(menu_options))])
        print(
            'Choose the phone book:\n'
            f'{output_string}\n'
        )
        return menu_options

    @staticmethod
    def show_book_menu(book_file: Path) -> list[str]:
        menu_options = [
            'Show all contacts',
            'Find contact',
            'Add contact',
            'Update contact',
            'Remove contact',
            'Save book',
            'Back',
            'Exit'
        ]
        output_string = '\n'.join([f'{i + 1}. {menu_options[i]}' for i in range(len(menu_options))])
        print(
            f'{str(book_file)}\n'
            f'{output_string}\n'
        )
        return menu_options

    @staticmethod
    def show_input(prompt: str) -> input:
        return input(f'{prompt}: ')

    @staticmethod
    def show_message(message: str):
        print(message)

    @staticmethod
    def show_wrong_option_message():
        print('Wrong option!')

    @staticmethod
    def show_contacts(contacts: list[Contact] | tuple[Contact]):
        if not contacts:
            print('No contacts')
        else:
            for contact in contacts:
                contact_attrs = [
                    f'Id: {contact.id}',
                    f'Name: {contact.name}',
                    f'Surname: {contact.surname}',
                    f'Phone: {contact.phone}',
                    f'Comment: {contact.comment}',
                ]
                print(', '.join(contact_attrs))
