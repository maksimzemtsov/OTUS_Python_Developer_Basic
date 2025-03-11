import pytest
from homework2.model import Contact, PhoneBook, write_to_file, read_contacts_from_file


def test_add_contact(phonebook):
    contact = Contact('Testovskiy', 'Userovskiy', '123456789', 'Chill guy')
    phonebook.add_contact(contact)
    assert contact in phonebook.contacts


@pytest.mark.parametrize('query, expected', [
    ('Sergio', True),
    ('SERGIO', True),
    ('Ser', True),
    ('Pharell', True),
    ('PHARELL', True),
    ('Phar', True),
    ('123456789', True),
    ('1234', True),
    ('Dolzhen deneg', True),
    ('DOLZHEN deneg', True),
    ('Dol', True),
    ('Victor', False)
])
def test_find_contact(phonebook, query, expected):
    contact = Contact('Sergio', 'Pharell', '123456789', 'Dolzhen deneg')
    phonebook.add_contact(contact)
    result = phonebook.find_contact(query)
    assert (len(result) > 0) == expected


def test_update_contact(phonebook):
    contact = Contact('Sergio', 'Pharell', '123456789', 'Dolzhen deneg')
    phonebook.add_contact(contact)
    PhoneBook.update_contact(contact, 'Ivan', 'Ivanov', '77777777', 'Nice guy')
    assert contact.name == 'Ivan'
    assert contact.surname == 'Ivanov'
    assert contact.phone == '77777777'
    assert contact.comment == 'Nice guy'


def test_remove_contact(phonebook):
    contact = Contact('Sergio', 'Pharell', '123456789', 'Dolzhen deneg')
    phonebook.add_contact(contact)
    phonebook.remove_contact(contact)
    assert contact not in phonebook.contacts


def test_file_operations(phonebook, temp_file):
    name = 'Sergio'
    surname = 'Pharell'
    number = '123456789'
    comment = 'Dolzhen deneg'
    contact = Contact(name, surname, number, comment)
    phonebook.add_contact(contact)
    write_to_file(phonebook)
    new_contacts = read_contacts_from_file(temp_file)
    assert (len(new_contacts) > 0) == 1
    contact = new_contacts[0]
    assert (contact.name == name and
            contact.surname == surname and
            contact.phone == number and
            contact.comment == comment)


@pytest.mark.parametrize('name, surname, phone, comment', [
    ('', 'Pharell', '123456789', 'Dolzhen deneg'),
    ('Sergio', '', '123456789', 'Dolzhen deneg'),
    ('Sergio', 'Pharell', '', 'Dolzhen deneg'),
    ('Sergio', 'Pharell', '123456789', ''),
    ('', '', '', '')
])
def test_adding_contacts_with_empty_fields(phonebook, name, surname, phone, comment):
    with pytest.raises(ValueError):
        contact = Contact(name, surname, phone, comment)
        phonebook.add_contact(contact)


def test_find_nonexisting_contact(phonebook):
    result = phonebook.find_contact('Blabla')
    assert len(result) == 0


def test_remove_nonexisting_contact(phonebook):
    contact = Contact('Blabla', 'Blabla', '777777', 'Blabla')
    with pytest.raises(ValueError):
        phonebook.remove_contact(contact)
