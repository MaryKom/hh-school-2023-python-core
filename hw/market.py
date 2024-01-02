from decorator import timer
class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = {} if wines is None else {wine.title: wine for wine in wines}
        self.beers = {} if beers is None else {beer.title: beer for beer in beers}

    @timer
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.wines | self.beers

    @timer
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        drinks = list(self.wines.values()) + list(self.beers.values())
        sorted_drinks = sorted(drinks, key=lambda drink: drink.title)
        return sorted_drinks

    @timer
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        drinks = list(self.wines.values()) + list(self.beers.values())
        if from_date is None and to_date is None:
            return None
        elif from_date is None:
            filter_drinks = [drink for drink in drinks if drink.production_date <= to_date]
        elif to_date is None:
            filter_drinks = [drink for drink in drinks if from_date <= drink.production_date]
        else:
            filter_drinks = [drink for drink in drinks if from_date <= drink.production_date <= to_date]
        sorted_drinks = sorted(filter_drinks, key=lambda drink: drink.production_date)
        return sorted_drinks
