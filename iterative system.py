## Python for loop to iterate through the letters in a word
# for i in "The Royal Colosseum":
#     print(i)
#
# for i in "The Royal Colosseum":
#     print(i, end="")

##Python for loop using the range() function
# for j in range(10):
#     print(j)

##Python for loop to iterate through a list
# AnimalList = ['Cat', 'Dog', 'Tiger', 'Cow']
# for x in AnimalList:
#     print(x, end=" ")
#
#     print(x)
##Python for loop to iterate through a dictionary
# programmingLanguages = {'J': 'Java', 'P': 'Python'}
# for key in programmingLanguages.keys():
#     print(key, programmingLanguages[key])

# #Python for loop using the zip() function for parallel iteration
# a1 = ['(a)', '(b)', '(c)']
# b2 = ['Python', 'Java', 'CSharp']
# c3 = [1, 2, 3]
# for i, j, k in zip(a1, b2, c3):
#     print(i, j, k)

# #Using else statement inside a for loop in Python
# flowers = ['Jasmine', 'Lotus', 'Rose', 'Sunflower']
# for m in flowers:
#     print(m)
# else:
#     print('Done')

# #Nested for loops in Python (one loop inside another loop)
# list1 = [5, 10, 15, 20]
# list2 = ['Tomatoes', 'Potatoes', 'Carrots', 'Cucumbers']
#
# for x in list1:
#     for y in list2:
#         print(x, y)

# #Using break statement inside a for loop in Python
# vehicles = ['Car', 'Cycle', 'Bus', 'Tempo']
#
# for v in vehicles:
#     if v == "Tempo":
#         break
#     print(v)

# #Python for loop to count the number of elements in a list
# numbers = [12, 3, 56, 97, 89, 90]
# count = 0
#
# for x in numbers:
#     count += 1
#
# print(count)

# #Python for loop to find the sum of all numbers in a list
# numbers = [12, 3, 56, 67, 89, 90]
# sum = 0
#
# for x in numbers:
#     sum += x
#
# print(sum)

# #Python for loop to copy elements from one list to another
# list1 = ['Mango', 'Banana', 'Orange']
# list2 = ['Banana']
# for i in list1:
#     list2.append(i)
#
# print(list2)

# Python for loop to find the maximum element in a list
numbers = [1, 4, 50, 80, 12]
max = 0

for n in numbers:
    if(n > max):
        max = n

print(max)