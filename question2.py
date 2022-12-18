# Q1) Take an integer input and check if the number is a perfect square
# Q2) Take an integer x and check if x(x+1)(x+2)....(x+n) where n is x-1 is even or odd
# Q3) Take an integer x and check if the sum of all its digits is greater or lesser or equal to the product of all its digits

#for comment - select-> command+/

# Q1)
# n = int(input())
# a =n//2
# for i in range(1, a+1):
#     if i*i == n:
#         print("perfect sqaure")
#         break
# else:
#     print("not a perfec square")

# Q)3
x = int(input())
n = x - 1
product = x
for i in range(1, n+1):
    product*=(x+i)
print(product)
if product % 2 ==0:
    print("Even")
else:
    print("odd")


