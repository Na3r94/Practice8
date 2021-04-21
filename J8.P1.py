class Fraction:
    def __init__(self,ss,mm):
        self.s = ss
        self.m = mm

    def mul(self,other):
        result = Fraction(None,None)
        result.s = self.s * other.s
        result.m = self.m * other.m
        return result

    def sum(self,other):
        result = Fraction(None,None)
        result.s = self.s * other.m + self.m * other.s
        result.m = self.m * other.m
        return result

    def sub(self,other):
        result = Fraction(None,None)
        result.s = self.s * other.m - self.m * other.s
        result.m = self.m * other.m
        return result

    def div(self,other):
        result = Fraction(None,None)
        result.s = self.s * other.m
        result.m = self.m * other.s
        return result


    def show(self):
        print(self.s,'/',self.m)

s1 = int(input('Please enter s1 :'))
m1 = int(input('Please Enter m1 :'))
s2 = int(input('Please enter s2 :'))
m2 = int(input('Please Enter m2 :'))
a = Fraction(s1,m1)
b = Fraction(s2,m2)
while True:
    print('Choose your operator : \n1 - sum \n2 - sub \n3 - mul \n4 - div\n0 - Exit')
    choice = int(input())
    if choice == 1:
        a.sum(b).show()
    elif choice == 2 :
        a.sub(b).show()
    elif choice == 3 :
        a.mul(b).show()
    elif choice == 4 :
        a.div(b).show()
    elif choice == 0:
        exit()

