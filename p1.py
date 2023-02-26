import datetime as dt

# В эту переменную запишите формат для
# преобразования даты
FORMAT = '%d.%m.%Y'


# Добавьте в объявление функции ещё один параметр - имя
def get_days_to_birthday(name, date_birthday):
    # Преобразуйте полученную строку с датой в объект нужного типа
    date_birthday = dt.datetime.strptime(date_birthday, FORMAT)

    today = dt.datetime.today()
    today_year = today.year
    date_birthday_1 = date_birthday.replace(year=today_year)

    if date_birthday_1 < today:
        date_birthday_1 = date_birthday_1.replace(year=today.year + 1)

    days_to_birthday = date_birthday_1 - today
    result = days_to_birthday.days
    return result


birthdays = {
    'Лера': '16.05.2015',
    'Максим': '16.12.2011',
    'Толя': '12.06.2016'
}

# Напечатайте результат вызова функции get_days_to_birthday()
# для каждой пары из списка birthdays
for key in birthdays:
    days = get_days_to_birthday(key, birthdays[key])
    print(f'{key}, до твоего дня рождения осталось дней: {days}')
