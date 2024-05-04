
class Date:
    second: int
    minute: int
    day: int
    month: int
    year: int

    def __init__(self, second, minute, day, month, year) -> None:
        self.second = second
        self.minute = minute
        self.day = day
        self.month = month
        self.year = year

    def convert_to_number_format(self):
        return self.second + self.minute * 60 + self.day * 24 * 60 * 60 + self.month * 31 * 24 * 60 * 60 + self.year * 365 * 24 * 60 * 60
