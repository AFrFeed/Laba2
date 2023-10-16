from datetime import datetime

class Period:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getSeconds(self):
        diff = self.end - self.start
        return diff.total_seconds()

    def getMinutes(self):
        diff = self.end - self.start
        return diff.total_seconds() / 60

    def getHours(self):
        diff = self.end - self.start
        return diff.total_seconds() / 3600

    def getDays(self):
        diff = self.end - self.start
        return diff.days

start = datetime(2023, 1, 2, 3, 4, 5)
end = datetime(2023, 5, 4, 3, 2, 1)
period = Period(start, end)
print(start,"==>",end)
print("Секунды =",period.getSeconds())
print("Минуты =",period.getMinutes())
print("Часы =",period.getHours())
print("Дни =",period.getDays())