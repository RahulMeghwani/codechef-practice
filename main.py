# Write a program which takes an input n and prints the cube of all even numbers till n
n = int(input())
for x in range(n):
    if x%2==0:
        print(x*x*x)
