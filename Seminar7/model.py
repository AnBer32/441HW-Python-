phone_book = []
path = 'phone_book.txt'


def get_phone_book():
    global phone_book
    return phone_book


def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)


def open_phone_book():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))


def save_phone_book():
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))


def change_contact(old_contact, new_contact):
    for i in range(len(phone_book)):
        if old_contact[0] == phone_book[i]:
            phone_book[i] = new_contact
            break


def delete_contact(contact):
    global phone_book
    for i in range(len(phone_book)):
        if contact[0] == phone_book[i]:
            phone_book.remove(phone_book[i])
            break


def search_contact(search: str):
    global phone_book
    search_results = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_results.append(line)
                break
    return search_results