from tabulate import tabulate
import uuid

def pause_after_action(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        input(': ')
    return wrapper

@pause_after_action
def save(book_content, file_name):
    for row in book_content:
        row.pop(0)
    book_strings = [str.join(';', row) for row in book_content]
    with open(f'./phone_books/{file_name}', 'w') as file:
        file.write(str.join('\n', book_strings))
    print('File was succesfully saved')


@pause_after_action
def show_all_items(book_content):
    print(tabulate(book_content, headers="firstrow", tablefmt="simple_grid"))

@pause_after_action
def find_item(book_content):
    query = input('Type the query: ')
    search_result = [book_content.pop(0)]
    for row in book_content:
        for value in row:
            if query.lower() in value.lower():
                search_result.append(row)
    if len(search_result) == 1:
        print('No search results')
    else:
        print(tabulate(search_result, headers="firstrow", tablefmt="simple_grid"))

@pause_after_action
def remove_item(book_content: list):
    query = input('Type an ID of row to delete: ')

    id_index_row = book_content[0].index('id')
    for i in range(len(book_content) - 1):
        if book_content[i + 1][id_index_row] == query:
            deleted_row = book_content.pop(i + 1)
            print(f'Row "{deleted_row}" was deleted')
            break
    else:
        print('No row with such ID')

@pause_after_action
def add_item(book_content):
    column_names = book_content[0]
    column_names.remove('id')
    example_string = str.join(';', column_names)
    new_row = input(f'Enter person data in format {example_string} \n: ')
    if row := make_new_row(new_row, len(column_names)):
        book_content.append(row)
        print(f'Row was succesfully added to the phone book')

def make_new_row(row, columns_count):
    row = list(map(lambda x: x.strip(), row.split(';')))
    if len(row) != columns_count:
        print(f'You entered invalid count of parameters: {len(row)}. Valid is {columns_count}')
    else:
        row.insert(0, str(uuid.uuid4()))
        return row

@pause_after_action
def update_item(book_content):
    query = input('Type an ID of person to update: ')
    columns = book_content[0]
    id_index_row = columns.index('id')

    # Find row
    chosen_row = find_row_in_book_with_id(book_content, query, id_index_row)
    if not chosen_row:
        return

    params_to_update = input('Enter in format param1, param2, param3 = value1, value2, value3')

    result = validate_book_update_input(params_to_update, columns)
    if not result:
        return

    params, values = result

    # Change original row
    for param, value in zip(params, values):
        param_index = book_content[0].index(param)
        chosen_row[param_index] = value

def find_row_in_book_with_id(book_content, query, id_index_row):
    for i in range(len(book_content) - 1):
        if book_content[i + 1][id_index_row] == query:
            chosen_row_index_in_book = i + 1
            return book_content[chosen_row_index_in_book]
    else:
        print('No row with such ID')
        return

def validate_book_update_input(params_to_update, columns):
    if params_to_update.count('=') == 1:
        params = list(map(lambda x: x.strip(), params_to_update.split('=')[0].split(',')))
        values = list(map(lambda x: x.strip(), params_to_update.split('=')[1].split(',')))
        if len(params) != len(values):
            print('Lengths of "params" and "values" must match')
            return
        for param in params:
            if param not in columns:
                print('No such parameters')
                return
        return params, values
    else:
        print('Invalid input')
        return