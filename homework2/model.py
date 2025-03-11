from itertools import count
from pathlib import Path
index_counter = count()


class Contact:
    def __init__(self, name: str, surname: str, phone: str, comment: str):
        self.id = str(next(index_counter))
        if not name:
            raise ValueError('Name cant be empty')
        if not surname:
            raise ValueError('Surname cant be empty')
        if not phone:
            raise ValueError('phone cant be empty')
        if not comment:
            raise ValueError('comment cant be empty')
        self.name = name.strip()
        self.surname = surname.strip()
        self.phone = phone.strip()
        self.comment = comment.strip()


class PhoneBook:
    def __init__(self, book_file: Path):
        self.book_file = book_file
        self.contacts = read_contacts_from_file(book_file)

    def find_contact(self, query: str) -> list[Contact]:
        founded = []
        query = query.lower()
        for contact in self.contacts:
            if (query in contact.id.lower() or
                    query in contact.name.lower() or
                    query in contact.surname.lower() or
                    query in contact.phone.lower() or
                    query in contact.comment.lower()):
                founded.append(contact)

        return founded

    def find_contact_with_id(self, query: str) -> tuple[Contact]:
        for contact in self.contacts:
            if query == contact.id:
                return (contact,)

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def remove_contact(self, contact: Contact):
        self.contacts.remove(contact)

    @staticmethod
    def update_contact(
            contact: Contact, 
            new_contact_name: str, 
            new_contact_surname: str, 
            new_contact_phone: str, 
            new_contact_comment: str
    ):
        if new_contact_name != '':
            contact.name = new_contact_name
        if new_contact_surname != '':
            contact.surname = new_contact_surname
        if new_contact_phone != '':
            contact.phone = new_contact_phone
        if new_contact_comment != '':
            contact.comment = new_contact_comment


def read_contacts_from_file(file: Path) -> list[Contact]:
    contacts = []
    if str(file).split('.')[-1] == 'txt':
        with open(file, 'r') as file:
            for string in file.readlines():
                params = string.split(';')
                contacts.append(Contact(params[0], params[1], params[2], params[3]))
    return contacts


def write_to_file(book: PhoneBook):
    with open(book.book_file, 'w') as file:
        file_strings = [
            f'{contact.name};{contact.surname};{contact.phone};{contact.comment}' for contact in book.contacts
        ]
        file.write('\n'.join(file_strings))
