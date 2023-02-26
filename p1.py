from datetime import datetime as dt
# В эту переменную запишите формат для
# преобразования даты
FORMAT = '%d.%m.%Y'

# Добавьте в объявление функции ещё один параметр - имя
def get_days_to_birthday(names, date_birthday):
    # Преобразуйте полученную строку с датой в объект нужного типа
    date_birthday = dt.strptime(date_birthday, FORMAT)
    date_birthday_1 = date_birthday.date()

    today = dt.today()
    today_year = today.year
    date_birthday_1 = date_birthday.replace(year=today_year)

    if date_birthday_1 < today:
        date_birthday_1 = date_birthday_1.replace(year=today.year + 1)

    days_to_birthday = date_birthday_1 - dt.today()
    result = days_to_birthday.days
    return f'{names}, до твоего дня рождения осталось дней: {result}'


birthdays = [
    ('Лера', '16.05.2015'),
    ('Максим', '16.12.2011'),
    ('Толя','12.06.2016')
]

# Напечатайте результат вызова функции get_days_to_birthday()
# для каждой пары из списка birthdays
dictionar = dict(birthdays)
for keys in dictionar:
    print(get_days_to_birthday(keys, dictionar[keys]))