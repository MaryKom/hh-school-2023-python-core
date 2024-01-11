class Wine:
    def __init__(self, title=None, production_date=None) -> None:
        self.title = title
        self.production_date = production_date

    def __str__(self):
        production_date = "None" if self.production_date is None else self.production_date.strftime("%Y-%m-%d")
        title = "None" if self.title is None else self.title
        return "(title=" + title + ", production_date=" + production_date + ")"
