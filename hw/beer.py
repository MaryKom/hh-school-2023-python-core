class Beer:
    def __init__(self, title=None, production_date=None) -> None:
        self.title = title
        self.production_date = production_date

    def __str__(self):
        production_date = "None" if self.production_date is None else self.production_date.strftime("%Y-%m-%d")
        return "(title=" + self.title + ", production_date=" + production_date + ")"
