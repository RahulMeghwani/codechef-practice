alice = int(input())
bob = int(input())
charlie = int(input())
if alice>bob and alice>charlie:
    print("alice")
elif bob>alice and bob>charlie:
    print("bob")
elif charlie>alice and charlie>bob:
    print("charlie")
else:
    print(0)
    