a = int(input())
b = int(input())
c = int(input())
highest = 0
if a>b and a>c: 
    highest = a
    if b>c:
        print(b)
    else:
        print(c)
elif b>a and b>c:
    highest = b
    if a>c:
        print(a)
    else:
        print(c)
else: 
    highest = c
    if a>b:
        print(a)
    else:
        print(b)
        
