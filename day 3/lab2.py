a  = int(input("enter your first sub marks: "))
b = int(input("enter your second sub marks: "))
c = int(input("enter your third sub marks: "))
d = int(input("enter your fourth sub marks: "))
c = a+b+c+d
e = (c /400)*100
print("total: ", c)
print("percentage: ", e)
if e > 70:
    print("distinction")
elif e >60 and e <70:
    print("first devison ")
elif e > 40 and e < 60:
    print("pass")
else:
    print("fail")

