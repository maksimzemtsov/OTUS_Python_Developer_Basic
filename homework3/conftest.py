import pytest
from homework2.model import PhoneBook


@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / 'test_contacts.txt'
    file.touch()
    return file


@pytest.fixture
def phonebook(temp_file):
    return PhoneBook(temp_file)
