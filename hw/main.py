from wine import Wine
from beer import Beer
from market import Market

from datetime import datetime

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""

wines = [
    Wine("Cabernet", datetime.strptime('2023-12-24', '%Y-%m-%d')),
    Wine("Sovinion", datetime.strptime('2023-12-15', '%Y-%m-%d')),
    Wine("Izabel", datetime.strptime('2020-05-06', '%Y-%m-%d')),
    Wine("Merlot", datetime.strptime('2015-01-26', '%Y-%m-%d')),
]
beers = [
    Beer("Ochakovo", datetime.strptime('2023-05-05', '%Y-%m-%d')),
    Beer("Melnik", datetime.strptime('2020-03-12', '%Y-%m-%d')),
    Beer("Tuborg", datetime.strptime('2021-07-07', '%Y-%m-%d')),
    Beer("Bavaria", datetime.strptime('2022-09-29', '%Y-%m-%d')),
]

market = Market(wines, beers)

print("             Drinks with title:")
drink = market.has_drink_with_title("Ochakovo")
print("Ochakovo exists: " + str(drink))
drink = market.has_drink_with_title("Merlot")
print("Merlot exists: " + str(drink))
drink = market.has_drink_with_title("Abc")
print("Abc exists: " + str(drink))

print("             Drinks sorted by title:")
drinks_by_title = market.get_drinks_sorted_by_title()
for drink in drinks_by_title:
    print(drink)

print("             Drinks sorted by production_date:")
from_date = datetime.strptime('2022-01-01', '%Y-%m-%d')
to_date = datetime.strptime('2023-12-31', '%Y-%m-%d')
drinks_by_production_date = market.get_drinks_by_production_date(from_date, to_date)
for drink in drinks_by_production_date:
    print(drink)
