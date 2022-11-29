from stud_csv import file_open, insert, show_rows, save, drop_by_arg, find, students_fullnames_by_group

FILENAME = "data (1).csv"

MENU = {
    '1': 'Открыть файл',
    '2': 'Добавить',
    '3': 'Удалить',
    '4': 'Поиск по ФИО',
    '5': 'Вывести из группы',
    '6': 'Сохранить в файл',
    '7': 'Вывести данные',
    '8': 'Перевести на курс',
    '0': 'Меню',
    'exit': 'Выход'
}
for k, v in MENU.items():
    print(k, '-', v)


while True:
    action = input('>_')
    if action == '1':
        file_open(FILENAME)
    elif action == '2':
        insert(input('ФИО: '), input('пол: '), input('возраст: '), input('телефон: '), input('почта: '), input('группа: '), input('курс: '))
    elif action == '3':
       print(drop_by_arg(input("Значение: "), input("Колонка: ")))
    elif action == '4':
         find(input("Значение: "), input("Колонка: "))
    elif action == '5':
        group = input("Группа: ")
        students_fullnames_by_group(group)
    elif action == '6':
        save(FILENAME)
    elif action == '7':
        show_rows()
    elif action == '0':
        for k, v in MENU.items():
            print(k, '-', v)
    elif action == 'exit':
        break
