x = 0
d =0
a = int(input("enter a starting number: "))
b =int(input("enter a end nummber: "))
for i in range(a,b):
    if i%2 == 0 :
        x +=1
    else:
        d +=1
print(f"{x} even numbers")
print(f"{d} odd numbers")
