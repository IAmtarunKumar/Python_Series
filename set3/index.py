# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.

# - *Input*: [("John", 25), ("Jane", 30)]

# - *Output*: "John is 25 years old. Jane is 30 years old."

list = [("John", 25), ("Jane", 30)]

print(list[0][0]+" is "+ str(list[0][1])+ " years old. " + list[1][0] + " is " + str(list[1][1]) + " year old. ")




# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.

# - *Input*: Add "John": 25, Update "John": 26, Delete "John"

# - *Output*: "{}, {'John': 26}, {}"

dic = {}

dic["jone"]= 25
dic["jone"] = 26

del dic["jone"]

print(dic)




# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.

# - *Input*: [2, 7, 11, 15], target = 9

 # - *Output*: "[0, 1]"

list = [2, 7, 11, 15]
target = 9
start = 0
end =len(list)-1
print(end)

list.sort()

while(start<end):
    sum = list[start]+list[end]
    if(sum>target):
        end=end-1
    elif(sum<target):
        start=start+1
    else:
        print([start,end])
        break;


# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.

# - *Input*: "madam"

# - *Output*: "The word madam is a palindrome."

word = "madam"
reverse = ""
for i in range(len(word)-1,-1,-1):
    reverse+=word[i]

if(word==reverse):
    print("the word",word,"is a palindrome")
else:
    print("the word",word,"is not palindrome")

# 1. **Selection Sort**: Implement the selection sort algorithm in Python.

# - *Input*: [64, 25, 12, 22, 11]

# - *Output*: "[11, 12, 22, 25, 64]"

list = [64, 25, 12, 22, 11]
min = list[0]

num = len(list)
i=0
arr = []
for i in range(num):
    for item in range(num):
        if list[item]<min:
            min=item
    
    arr.append(min)
    # list[min]=5
    i=i+1

print(arr)

