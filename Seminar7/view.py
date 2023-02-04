def main_menu():
    commands = ['Показать все контакты',
                'Открыть файл',
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Найти контакт',
                'Выйти из программы']
    print('Выберите пункт меню: ')
    for i in range(len(commands)):
        print(f'\t{i + 1}. {commands[i]}')
    while True:
        try:
            user_input = int(input('\nВведите пункт меню: '))
            if 0 < user_input < 9:
                break
            else:
                print('\nВыберите пункты в диапазоне от 1 до 8')
        except:
            print('\nТолько цифры от 1 до 8!!!')
    return user_input


def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(f'{item[0]} {item[1]} ({item[2]})')
    else:
        print('Телефонная книга пустая или не загружена')


def load_success():
    print('Телефонная книга загружена успешно!!!')


def save_success():
    print('Телефонная книга сохранена успешно!!!')


def new_contact():
    name = input('Введите Имя и Фамилию контакта: ')
    phone = input('Введите номер контакта: ')
    comment = input('Введите комментарий к контакту: ')
    return name, phone, comment


def new_contact_success():
    print('Новый контакт добавлен!'
          '\nВыберите 3 пункт для сохранения телефонной книги!')


def find_contact():
    search = input('Введите искомое значение: ')
    return search


def change_contact():
    contact = input('Введите искомый контакт, который хотите изменить: ')
    return contact


def change_contact_success():
    print('Контакт изменен!'
          '\nВыберите 3 пункт для сохранения телефонной книги!')


def del_contact():
    contact = input('Введите искомый контакт, который хотите удалить: ')
    return contact


def del_contact_success():
    print('Контакт удален!'
          '\nВыберите 3 пункт для сохранения телефонной книги!')