from Jalase8.Date import Date
while True:
    print('Enter the First Date:')
    y1 = int(input('Please Enter the year(1) :'))
    m1 = int(input('Please Enter the month(1) :'))
    d1 = int(input('Please Enter the day(1) :'))
    a = Date(y1,m1,d1)
    while True:
        print('1 - Sum two Date\n2 - Sub two Date\n3 - Get month\n4 - Leap Year\n5 -Date Validation\n6 - Age calc\n7 - Change First Date\n0 - Exit')  
        choice = int(input('Please Enter number : '))
        if choice == 1 or choice == 2 or choice == 6:
            print('Enter the second Date:' )
            
            y2 = int(input('Please Enter the year(2) :'))
            m2 = int(input('Please Enter the month(2) :'))
            d2 = int(input('Please Enter the day(2) :'))
            b = Date(y2,m2,d2)
            if choice == 1:
                a.add(b).show()
            elif choice == 2 or choice == 6 :
                a.sub(b).show()
        
        elif choice == 3:
            a.getMonthName()
        elif choice == 4:
            a.isLeapYear()
        elif choice == 5:
            a.isValidDate
        elif choice == 7:
            break
        elif choice == 0:
            exit()


