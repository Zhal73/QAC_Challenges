def timetable(n):
    line =""
    for row in range(1,n+1):
        for column in range(1,n+1):
            line = line + str(row * column) + "\t"
        line = line +"\n"
    return line

number = int(input("Enter table width: "))
print(timetable(number))