from date_create import *
# Вывод всей книги
def print_contacts():
    ''''Вывод записей'''
    # with open('phonebook.txt', 'r', encoding='utf-8') as file:
    #     print('******************************************')
    #     print(file.read())
    #     print('******************************************')
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read().rstrip().split('\n\n')
        for nn, contact in enumerate(contacts_str, 1):
            print(f'{nn}. {contact} \n')
    return contacts_str
            
        
# Функция поиска
def search_contact():
    print(
            'Варианты поиска:\n'
            '1. По фамилии \n'
            '2. По имени\n'
            '3. По отчеству \n'
            '4. По номеру\n'
            '5. По городу\n'
            )
    index_var = int(input('Ваш выбор: '))-1
    search = input('Введите данные для поиска: ')
    print()
    with open('phonebook.txt', 'r', encoding='utf8') as file:
        contacts_str = file.read()
    contacts_list = contacts_str.rstrip().split('\n\n')
    for contact_str in contacts_list:
        contact_list = contact_str.replace('\n',' ').split(' ')
        if search in contact_list[index_var]:
            print(f'\n {contact_str} \n')
            print()
            
# Функция получения пользовательского ввода для добавления контакта

def create_contact():
    
    surname = surname_input()
    name = name_input()
    patronymic = patronymic_input()
    phone = phone_input()
    adress = address_input()
    return f'{surname} {name} {patronymic} {phone}\n{adress}\n\n'

# Функция записи нового контакта в файл

def write_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
        print('\n Контакт добавлен! \n')
        
# Функция копирования контакта в новый файл
        
def copy_contact ():
    contacts_str = print_contacts()
    index_contact = int(input('Контакт из какой строки скопировать?: '))
    print()
    for nn, contact in enumerate(contacts_str, 1):
        if index_contact == nn:
            print(f'Контакт:   "{nn}. {contact}" скопирован!\n')
            with open('newbook.txt', 'a', encoding='utf-8') as file:
                file.write(f'{contact} \n')
            file.close()
