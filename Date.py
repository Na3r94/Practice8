class Date():
    def __init__(self,year,month,day):
        self.y = year
        self.m = month
        self.d = day
    def add(self,other):
        result = Date(None,None,None)
        result.d = self.d + other.d
        result.m = self.m + other.m
        if result.d >30:
            result.d -= 30
            result.m +=1
        result.y = self.y + other.y
        if result.m > 12:
            result.m -= 12
            result.y += 1
        return result

    def getMonthName(self):
        month = ['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar','Mehr','Aban','Azar','Dey','Bahman','Esfand']
        print(month[self.m-1])
    def isLeapYear(self):
        if self.y % 4 == 3:
            print('True')
        else:
            print('False')

    def sub(self,other):
        result = Date(None,None,None)
        result.d = self.d - other.d
        result.m = self.m - other.m
        if result.d <1:
            result.d += 30
            result.m -= 1
        result.y = self.y - other.y
        if result.m < 1 :
            result.m += 12
            result.y -= 1

        return result

    def isValidDate(self):
        if 0 < self.d < 31 and 0 < self.m < 13 and 0 < self.y < 10000:
            pass
        else:
            print('False')


    def show(self):
        print(self.y,'/',self.m,'/',self.d)
