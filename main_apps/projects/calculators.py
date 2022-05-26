"""
Раздичные калькуляторы
1 Калькулятор возраста. Пользователь вводит дату рождения, а в ответ автоматически получает возраст.
2 отслеживаниe курса валюты Dollar_RUB
при желании можно расширить кол-во валют и добавить другие курсы(металы, акции),
а также сделать отправку на личную почту отчетов об изменениях

"""
import datetime
import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup  # Модуль для работы с HTML


def calculate_age(year):
    now = datetime.datetime.now()
    year_birth = int(year)
    return now.year - year_birth


# Ссылка на нужную страницу
DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
# Заголовки для передачи вместе с URL
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

# Для получения курса валюты
def get_currency_DOLLAR_RUB():
    """получает курса валюты Dollar_RUB с Гугла"""
    # Парсим всю страницу
    full_page = requests.get(DOLLAR_RUB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    # Получаем нужное для нас значение и возвращаем его
    convert_DOLLAR_RUB = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    convert_DOLLAR_RUB = float(convert_DOLLAR_RUB[0].text.replace(",", "."))
    return convert_DOLLAR_RUB


def calculate_currency_DOLLAR_RUB(amount):
    """
    т.к. рекомендуют всю логику выносить за Вьюхи
    Упрощеная функция без Decimal для вычисления  суммы Руб к Доллару
    """
    amount = float(amount)
    calc = amount / get_currency_DOLLAR_RUB()
    return round(calc, 2)


if __name__ == '__main__':
    currency_DOLLAR_RUB = get_currency_DOLLAR_RUB()
    print(currency_DOLLAR_RUB, type(currency_DOLLAR_RUB))
    print('Input SUM RUB:')
    sum_RUB = int(input())
    print(calculate_currency_DOLLAR_RUB(sum_RUB), type(calculate_currency_DOLLAR_RUB(sum_RUB)))


