 num = int(input("enter a number: "))
factorial = 1
if num <0:
    print("doesnot exist for negative numbers.")
elif num == 0:
    print(f"{factorial}  if factorial of 0.")
else:
    for i in range(1,num+1):
        factorial = i * factorial
    print(f"{factorial} is facorial of{num} .")
    