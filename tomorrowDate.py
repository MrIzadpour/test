date = input("Please enter your date by using / : ")

if date.count("/") == 2:
    year, month, day = date.split("/")

else:
    raise Exception("Invalid input!!!")

if len(year) == 4 and len(month) <= 2 and len(day) <= 2:
    day = int(day)
    month = int(month)
    year = int(year)

    remaining = [1, 5, 9, 13, 17, 22, 26, 30]
    intercalary = False

    if (year % 33) in remaining:
        intercalary = True
        
    day += 1

    if 1 <= month <= 6:
        if day > 31:
            month += 1
            day = 1
    elif 6 <= month <= 12:
        if month == 12 and not intercalary:
            if day > 29:
                year += 1
                month = 1
                day = 1

        elif month == 12 and intercalary:
            if day > 30:
                year += 1
                month = 1
                day = 1

        if day > 30:
            month += 1
            day = 1

    print(year, month, day, sep="/")

else:
    print("Invalid input !!!")
