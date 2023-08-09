### Problem **1: Print the following pattern**

# output 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num=7
bag=""
for i in range(1,num):
    bag=""
    for j in range(1, i):
        bag=bag+str(j)+" "
    
    print(bag)


# Problem 2: Display numbers from a list using loop

numbers = [12, 75, 150, 180, 145, 525, 50]

# output 
# 75
# 150
# 145

for num in numbers:
    if num % 5 == 0:
        if num > 500:
            break
        elif num > 150:
            continue
        else:
            print("Valid number:", num)
    else:
        print("Not divisible by 5:", num)


# Problem 3: Append new string in the middle of a given string

s1 = "Ault"
s2 = "Kelly"

# output =   AuKellylt


num = int(len(s1)/2)
s1 = list(s1)
s1.insert(num,s2)
print("".join(s1))


# Problem 4: Arrange string characters such that lowercase letters should come first

str1 = "PyNaTive"

# output : yaivePNT 

upperCase  =str1.upper()
# print(upperCase)
upperChar = ""
lowerChar = ""

for i in range(len(str1)):
    if(str1[i]==upperCase[i]):
        upperChar+=str1[i]
    else:
        lowerChar=lowerChar+str1[i]

print(lowerChar+upperChar)
       
### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.  

# Given
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# ouput 
# ['My', 'name', 'is', 'Kelly']

sentance = []
for i in range(len(list1)):
    word = list1[i]+list2[i]
    sentance.append(word)

print(sentance)


### Problem **6: Concatenate two lists in the following order**

# given
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# output 
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

sentance = []
for i in range(len(list1)):
    for j in range(len(list2)):
        word = list1[i]+" "+list2[j]
        sentance.append(word)

print(sentance)



### Problem **7: Iterate both lists simultaneously**

# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# output 
# 10 400
# 20 300
# 30 200
# 40 100

bag=""
for i in range(len(list1)):
    print(list1[i], list2[i])

    
### Problem **8: Initialize dictionary with default values**

# In Python, we can initialize the keys with the same values.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# # output
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
dictionary = {}
for i in range(len(employees)):
    dictionary[employees[i]]=defaults

print(dictionary)




### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

# output 
# {'name': 'Kelly', 'salary': 8000}

dictionary = {}

for item in keys:
    dictionary[item] = sample_dict[item]

print("Output is : " ,  dictionary)



### Problem **10: Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

tuple1 = (11, [22, 33], 44, 55)

# output 
# tuple1: (11, [222, 33], 44, 55)

for i in range(len(tuple1)):
    if type(tuple1[i])==list:
       tuple1[i][0]=222

print(tuple1)
    