# Lists - collections of heterogenous data types
# Lists = [...]

# variable name = [list]
my_list = ["Rahul", 18, 2003, 18]
# lists = 0, 1, 2 ...

# adding in list - .append()
my_list.append("Soham")

# Counting elements in a list - .count(value)
# print(my_list.count(18))

# Adding one list to another - .extend(list2)
new_list = ["Hello", "World", 69]
my_list.extend(new_list)

# Getting the first occurence of a value - .index(value)
# print(my_list.index(18))

# Adding a value to a specific location - .insert(index, value)
my_list.insert(1, "bag")

# Removing an item with specified index - .pop(index)
idx = my_list.index(18)
my_list.pop(idx)

# directly removing an item - .remove(item)
my_list.remove("Hello")

# print(my_list[1]) # prints 2nd item
# print(my_list[1:5])
# print(my_list)

# List slicing - list[start:end:step]
# Last elem - list[-1]
# All even - list[::2]
nums = [0, 1, 2, 6, 7, 8, 9, 10]
# print(nums[::2])

# List comprehension - [var for var in collection]
# nums = [x for x in range(6)]
# for x in range(6):
#     nums.append(x)

# Tuples - immutable
my_tuple = ("Rahul", 18, 2003)

# for n in nums:
#     if n%2==0:
        # print(n)

# List comprehension for even numbers
evens = [n for n in nums if n%2==0]
# print(evens)

# Dictionary - used to store key: value pairs
student_info = {
    "Name": "Rahul",
    "Age": 18,
    "DoB": 2003
    # is_eligible: True
}

# Printing keys = dict.keys()
# Values = dict.values()

student_info["Name"] = "Soham"
student_info["is_eligible"] = True
# print(student_info)

# Looping keys
# for x in student_info:
#     print(x)

# Looping values
# for x in student_info:
#     print(student_info[x])
# for x in student_info.values():
#     print(x)

# Looping both
# for x in student_info.items():
#     print(x)

# for temp_var in collection
# lst = [0, 1, 2, 3, 4, 5]
# for x in lst:
#     if x%2==0:
#         print(x)

# *
# **
# ***
# ****
# n = int(input())
# for x in range(1, n+1): # range(1, 5) -> [1, 2, 3, 4]
#     print("*"*x)
# for x in range(n-1, 0, -1): # range(5-1, 0, -1) -> [4, 3, 2, 1]
#     print("*"*x)

# while expression:
#   code
count = 5
while count > 0:
    print(count)
    count-=1
