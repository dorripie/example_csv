import csv

csv_file = []

# Открыть файл
def file_open(file_name):
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            csv_file.append(row)
        print("Файл открыт. Записей: ", len(csv_file))

# Добавление
def insert(fio, pol, age, tel, mail, group, well):
    try:
        mx = max(csv_file, key=lambda x: int(x['номер']))
        csv_file.append({'номер': int(mx['номер'])+1,
                         'ФИО': fio,
                         'пол': pol,
                         'возраст': age,
                         'телефон': tel,
                         'почта': mail,
                         'группа': group,
                         'курс': well})
    except Exception as e:
        return f"Ошибка при добавлении нового студента {e}"
    print("Данные добавлены")

# Сохранить в файл
def save(fine_name):
    with open(fine_name, 'w', encoding='utf-8', newline='') as file:
        columns = ['номер','ФИО','пол','возраст','телефон','почта','группа','курс']
        writer = csv.DictWriter (file, delimiter=";", fieldnames=columns)
        writer.writeheader()
        writer.writerows(csv_file)
        print('Данные сохранены')

# Вывод данных
def show_rows():
    if len(csv_file) > 0:
        print('{:<5}{:<25}{:<3}{:<3}{:<11}{:<20}{:<5}{:<1}'.format('номер','ФИО','пол','возраст','телефон','почта','группа','курс'))
        for el in csv_file:
            print('{:<5}{:<25}{:<3}{:<3}{:<11}{:<20}{:<5}{:<1}'.format(el['номер'], el['ФИО'], el['пол'], el['возраст'], el['телефон'],
                                                        el['почта'], el['группа'], el['курс']))
