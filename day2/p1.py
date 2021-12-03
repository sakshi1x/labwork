second = int(input("enter a time in seconds. : "))
min = second / 60
m = min//1

hrs = min / 60
h = hrs//1

day = hrs % 24
print(f"your desiered time is {day} day {h}hrs and {m}min" )
