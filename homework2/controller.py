from homework2.view import PhoneBookManagerInterface
from homework2.model import PhoneBook, write_to_file, Contact
from pathlib import Path


class PhoneBookManager:
    def __init__(self):
        self.view = PhoneBookManagerInterface()

    def book_menu(self, chosen_book) -> bool:
        book = PhoneBook(chosen_book)
        while True:
            menu_options = self.view.show_book_menu(book.book_file)
            usr_input = self.view.show_input('Choose option')
            if int(usr_input) not in range(1, len(menu_options) + 1):
                self.view.show_wrong_option_message()
                continue
            chosen_option = menu_options[int(usr_input) - 1]
            if chosen_option == 'Show all contacts':
                self.view.show_contacts(book.contacts)
            elif chosen_option == 'Find contact':
                query = self.view.show_input('Enter id, name, surname, phone or comment of contact')
                founded_contacts = book.find_contact(query)
                self.view.show_contacts(founded_contacts)
            elif chosen_option == 'Add contact':
                contact_name = self.view.show_input('Enter name')
                contact_surname = self.view.show_input('Enter surname')
                contact_phone = self.view.show_input('Enter phone')
                contact_comment = self.view.show_input('Enter comment')
                book.add_contact(Contact(contact_name, contact_surname, contact_phone, contact_comment))
            elif chosen_option == 'Update contact':
                query = self.view.show_input('Enter contact\'s id to update')
                contact = book.find_contact_with_id(query)
                self.view.show_contacts(contact)
                if not contact:
                    continue
                contact_name = self.view.show_input('Enter name (leave it empty if it not for change)')
                contact_surname = self.view.show_input('Enter surname (leave it empty if it not for change)')
                contact_phone = self.view.show_input('Enter phone (leave it empty if it not for change)')
                contact_comment = self.view.show_input('Enter comment (leave it empty if it not for change)')
                book.update_contact(contact[0], contact_name, contact_surname, contact_phone, contact_comment)
            elif chosen_option == 'Remove contact':
                query = self.view.show_input('Enter contact\'s id to remove')
                contact = book.find_contact_with_id(query)
                self.view.show_contacts(contact)
                if not contact:
                    self.view.show_message('There is not contact with such Id')
                    continue
                book.remove_contact(contact[0])
                self.view.show_message('Contact was removed')
            elif chosen_option == 'Save book':
                write_to_file(book)
            elif chosen_option == 'Back':
                return True
            elif chosen_option == 'Exit':
                return False

    def books_list_menu(self) -> bool:
        books_dir = Path('./phone_books')
        files = [file for file in books_dir.iterdir()]
        while True:
            menu_options = self.view.show_books_list(files)
            usr_input = self.view.show_input('Choose option')
            if int(usr_input) not in range(1, len(menu_options) + 1):
                self.view.show_wrong_option_message()
                continue
            chosen_option = menu_options[int(usr_input) - 1]
            if chosen_option == 'Exit':
                return False
            elif chosen_option == 'Back':
                return True
            else:
                status = self.book_menu(chosen_option)
                if not status:
                    return False

    def start_menu(self):
        while True:
            self.view.show_welcome_menu()
            usr_input = self.view.show_input('Choose option')
            if usr_input == '1':
                status = self.books_list_menu()
                if not status:
                    self.view.show_message('Exiting from Phone Book Manager...')
                    break
            elif usr_input == '2':
                self.view.show_message('Exiting from Phone Book Manager...')
                break
            else:
                self.view.show_wrong_option_message()

    def run(self):
        self.start_menu()
        