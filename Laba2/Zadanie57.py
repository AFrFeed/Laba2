import calendar

class Zate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def getWeekdayIndex(self):
        return calendar.weekday(self.year, self.month, self.day)

    def getWeekdayName(self):
        weekday_index = self.getWeekdayIndex()
        return calendar.day_name[weekday_index]

    def getMonthName(self):
        return calendar.month_name[self.month]

zate = Zate(2005, 2, 6)

print("Год",zate.getYear())
print("Месяц",zate.getMonth())
print("День",zate.getDay())
print("Число",zate.getWeekdayIndex())
print("День,название",zate.getWeekdayName())
print("Месяц,название",zate.getMonthName())