"""
Раздичные калькуляторы
1 Калькулятор возраста. Пользователь вводить дату рождения, а в ответ автоматически получает возраст.
"""
import datetime


def calculate_age(year):
    now = datetime.datetime.now()
    year_birth = int(year)
    return now.year - year_birth


