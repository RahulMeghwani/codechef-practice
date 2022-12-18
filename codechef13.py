x = int(input())
y = int(input())
chocolate = x*2
candy = y*5
if chocolate>candy:
    print("Chocolate")
elif candy>chocolate:
    print("candy")
elif chocolate == candy:
    print("Either")
else:
    print(0)
