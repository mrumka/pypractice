import datetime as dt  # Импортируйте необходимые модули

FORMAT = '%H:%M:%S'  # Запишите формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.

def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.
    if len(data) != 2 or None in data:
        return False
    return True

def check_correct_time(time):
    """Проверка корректности параметра времени."""
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше или равно самому большому значению ключа в словаре,
    # функция вернет False.
    # Иначе - True
    if len(storage_data) == 0 or time > max(storage_data):
        return True
    return False


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните  эту сумму.

    total = steps
    for i in storage_data:
        total += storage_data[i]
    return int(total)


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.
    dist = steps * STEP_M / 1000
    return dist


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    # В уроке «Последовательности» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени;
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float.
    time = float(current_time.minute) / 60 + current_time.hour
    spent_calories = (K_1 * WEIGHT + ((dist / time) ** 2 / HEIGHT) * K_2 * WEIGHT) * time * 60
    return spent_calories


def get_achievement(distance):
    """Получить поздравления за пройденную дистанцию."""
    # В уроке «Строки» вы описали логику
    # вывода сообщений о достижении в зависимости
    # от пройденной дистанции.
    # Перенесите этот код сюда и замените print() на return.
    if distance >= 6.5:
        achievement = 'Отличный результат! Цель достигнута.'
    elif distance >= 3.9:
        achievement = 'Неплохо! День был продуктивным.'
    elif distance >= 2:
        achievement = 'Маловато, но завтра наверстаем!'
    else:
        achievement = 'Лежать тоже полезно. Главное — участие, а не победа!'
    return achievement


def show_message(time, steps, distance, calories, achiev):  # Место для функции show_message.
    return print(f'''
  Время: {time}.
  Количество шагов за сегодня: {steps}.
  Дистанция составила {distance:.2f} км.
  Вы сожгли {calories:.2f} ккал.
  {achiev}''')


def accept_package(data):
    """Обработать пакет данных."""
    if check_correct_data(data) == False:
        return 'Некорректный пакет'

    pack_steps = int(data[1])  # Распакуйте полученные данные.
    pack_time = dt.datetime.strptime(data[0], FORMAT).time() # Преобразуйте строку с временем в объект типа time.

    if check_correct_time(pack_time) == False:  # Если функция проверки значения времени вернет False
        return 'Некорректное значение времени'

    storage_data[pack_time] = pack_steps

    day_steps = get_step_day(pack_steps)  # Запишите результат подсчёта пройденных шагов.
    dist = get_distance(day_steps)  # Запишите результат расчёта пройденной дистанции.
    spent_calories = get_spent_calories(dist, pack_time)  # Запишите результат расчёта сожжённых калорий.
    achievement = get_achievement(dist)  # Запишите выбранное мотивирующее сообщение.
    show_message(pack_time, day_steps, dist, spent_calories, achievement) # Вызовите функцию show_message().
        # Добавьте новый элемент в словарь storage_data.
      # Верните словарь storage_data.


# Данные для самопроверки.Не удаляйте их.
package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)

