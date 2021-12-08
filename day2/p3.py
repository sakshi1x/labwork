n = int(input("enter the number of minutes that is passed since midnight: "))
hrs  = n//60
min = n%60

while True:
    if hrs<=12:
        print(print(f"{hrs} : {min}"))
        break
    else:
        hrs -=12
