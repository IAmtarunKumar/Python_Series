# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.

# - *Input*: [("John", 25), ("Jane", 30)]

# - *Output*: "John is 25 years old. Jane is 30 years old."

list = [("John", 25), ("Jane", 30)]

print(list[0][0]+" is "+ str(list[0][1])+ " years old. " + list[1][0] + " is " + str(list[1][1]) + " year old. ")




# 2. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.

# - *Input*: Add "John": 25, Update "John": 26, Delete "John"

# - *Output*: "{}, {'John': 26}, {}"

dic = {}

dic["jone"]= 25
dic["jone"] = 26

del dic["jone"]

print(dic)




# 3. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.

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


# 4. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.

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

# 5. **Selection Sort**: Implement the selection sort algorithm in Python.

# - *Input*: [64, 25, 12, 22, 11]

# - *Output*: "[11, 12, 22, 25, 64]"

list = [64, 25, 12, 22, 11]
list.sort()
print(list)



# FizzBuzz: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".

for i in range(1,100+1):
    if(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0 and i%5==0):
        print("Fizz Buzz")
    else:
        print(i)



# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.

 # - *Input*: A text file named "input.txt" with the content "Hello world"

# - *Output*: A text file named "output.txt" with the content "Number of words: 2"


with open('input.txt' , 'r') as file:
    data = file.read()
    print("text inside file : " ,data)

    x =  data.split(" ")
    print("Number of words : " ,len(x))




# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
    # - *Input*: 5, 0
    # - *Output*: "Cannot divide by zero"

first = input("Enter your first Number : ")
second = input("Enter your second number : ")
print(first,second)
if(second=="0"):
    print("Connot divide by zero")
elif(first=="0"):
    print("Infinte")
else:
    ans = int(first)/int(second)
    print("Answer is" , ans)
