a = int(input())
b = int(input())
c = int(input())
max = 0
if a>b and a>c:
    max = a
elif b>a and b>c:
    max = b
elif c>a and c>b:
    max = c
else:
    print(0)
min = 0
if a<b and a<c:
    min = a
elif b<a and b<c:
    min = b
elif c<a and c<b:
    min = c
else:
    print(0)
print(max - min)
