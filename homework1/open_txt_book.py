import uuid

def open_txt_book(book_name: str) -> list[list] | None:
    with open(f'./phone_books/{book_name}', 'r') as file:
        phone_book = file.readlines()

    table = []
    for row in phone_book:
        values = row.split(';')
        values_list = [value.strip() for value in values]
        table.append(values_list)

    if not validate_table(table):
        return

    table[0].insert(0, 'id')
    for i in range(len(table) - 1):
        table[i + 1].insert(0, str(uuid.uuid4()))

    return table

def validate_table(table):
    for row in table:
        if len(row) != len(table[0]):
            return False
    else:
        return True