class Time:
    def __init__(self,hour,min,sec):
        self.h = hour
        self.m = min
        self.s = sec

    def sum(self,time2):
        result = Time(None,None,None)
        result.s = self.s + time2.s
        result.m = self.m + time2.m
        if result.s > 59:
            result.s -= 60
            result.m += 1
        result.h = self.h + time2.h
        if result.m > 59 :
            result.m -= 60
            result.h += 1
        return result
    def sub(self,time2):
        result = Time(None,None,None)
        result.s = self.s - time2.s
        result.m = self.m - time2.m
        if result.s < 0:
            result.s += 60
            result.m -= 1

        result.h = self.h - time2.h
        if result.m <0 :
            result.m += 60
            result.h -= 1
        return result

    def secToTime(self):
        pass
        # result = Time(None,None,None)
        # result.h = sec // 3600
        # sec2 = sec % 3600
        # result.m = sec2 // 60
        # result.s = sec2 % 60

        return result
    def timeToSec(self):
        result = self.h * 3600 + self.m * 60 + self.s
        print(result,'s')


    def show(self):
        print(self.h,':',self.m,':',self.s)




while True:
    print('Choice your operator : \n1 - sum two time\n2 - sub tow time\n3 - sec to time format\n4 - time to sec\n0 - Exit')
    Choice = int(input())
    if Choice == 1 or Choice == 2:
        e = int(input('saniye 1 ru vared konid : '))
        w = int(input('daqiqe 1 ru vared konid : '))
        q = int(input('saat 1 ru vared konid : '))
        a = Time(q,w,e)
        r = int(input('saniye 2 ru vared konid : '))
        t = int(input('daqiqe 2 ru vared konid : '))
        y = int(input('saat 2 ru vared konid : '))
        b = Time(y,t,r)

        if Choice == 1:
            a.sum(b).show()
        elif Choice == 2:
            a.sub(b).show()
    elif Choice == 3 :
        # sec = int(input('Saniye ru vared konid'))
        # sec.secToTime()
        pass

    elif Choice == 4 :
        hour_1 = int(input('Enter the Hour : '))
        min_1 = int(input('Enter the minute : '))
        sec_1 = int(input('Enter the second : '))
        time_1 = Time(hour_1,min_1,sec_1)
        time_1.timeToSec()

    elif Choice == 0:
        exit()