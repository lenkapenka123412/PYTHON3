from command_function import add_data, find_data, del_data, full_list_data #, edit_data

def menu():
    while True:
        print('Команды для работы со справочником: ')
        com = input("""
1. all — Показать все контакты
2. add — Добавить контакт
3. del — Удалить контакт
4. find — Найти контакт
5. stop — Закрыть программу
""")
        if com.lower() == '5':
            break
        if com.lower() == '2':
            add_data()
        if com.lower() == '3':
            str = input('Кого хотите удалить?: ')
            del_data(str)
        if com.lower() == '4':
            str = input('Кого ищете?: ')
            find_data(str)
        if com.lower() == '1':
            full_list_data()
        # if com.lower() == '5':
        #     edit_data(str)

        
