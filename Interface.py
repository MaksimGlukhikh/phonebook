from logger import *
def interface():
    with open('phonebook.txt', 'a'):
        pass
    user_input = None   
    while user_input != '4':
        print(
            'Что вы хотите сделать?\n'
            '1. Добавить контакт \n'
            '2. Вывод списка контактов\n'
            '3. Поиск контакта \n'
            '4. Выход'
            )
        user_input = input('Ваш выбор: ') 
        while user_input not in ('1', '2', '3', '4'):
            print('Некорректный ввод')
            user_input = input('Ваш выбор: ')
        print()
        match (user_input):
            case '1':
                write_contact()
            case '2':
                print_contacts()
            case '3': 
                search_contact()
        print()