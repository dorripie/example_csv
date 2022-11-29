from stud_csv import file_open

FILENAME = "data (1).csv"

MENU = {
    '1': 'Открыть файл',
    '2': 'Добавить',
    '3': 'Удалить',
    '4': 'Поиск по ФИО',
    '5': 'Вывести из группы',
    '6': 'Перевод на ку',
    '7': 'Вывести данные',
    '0': 'Меню',
    'exit': 'Выход'
}
for k, v in MENU.items():
    print(k, '-', v)


while True:
    action = input('>_')
    if action == '1':
        file_open(FILENAME)
    elif action == 'exit':
        break
