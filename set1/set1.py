#1
print("Hello world")



#2
# #type of variable
num = 10 #interger
print(num)
floatValue = 3.10 #float
print(floatValue)

isActive = True #boolean
print(isActive)

list = [10,20,30]  # work like array
print(list)
tuple = (10,20,30) # work like array but imutable
print(tuple)

set = {10,20,30,20} # work like array but not accept duplicate values
print(set)

dictionary = {"math" : 20 , "english" : 50}  # work like object
print(dictionary)



#3
list = [1,20,3,4,5,6,7,8,9,10]

list.append(11) # append item at last
print(list)

list.remove(5) #remove given value
print(list)

list.sort()
print(list)


#4

# sumAvg = input("Enter the list value : ")

# sum = 0
# avg = 0
# count = 0
# sumAvg = sumAvg.split(",")
# for item in sumAvg:
#     sum=int(sum)+int(item)
#     count = count+1


# avg = sum//count

# print("Total sum is : " + str(sum))
# print("Avrage : " , +  avg)

#5

name =  "Python"
i=len(name)
bag=""
while(i>0):
    bag=bag+name[i-1]
    i=i-1 
print(bag)

# 6

greet="Hello"
vowel = ["a","i","o","u","e"]

count = 0
for item in greet:
    for char in vowel:
        if(item==char):
            count=count+1

print("Number of vowel in string = " , count)

#7
#find prime number

num = input("Enter your number : ")
num  = int(num)
count=0
for item in range(2, num+1):
    if(num%item==0):
        count=count+1

if(count==1):
    print("It is a prime number")
else:
    print("It is not a Prime")

# 8

fact_value = input("Enter Your Number : ")
fact_value = int(fact_value)+1
fact = 1
for item in range(1,fact_value):
    fact = fact*item

print("The factorial is : ",fact)
    

# 9
# fibonacci series {sum of last to digit}

fibNum = input("Enter Your Number : ")
fibNum = int(fibNum)
fibonacci = [0,1]

for i in range(2,fibNum):
    next = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next)
    
print("Fibonacci sequence of length : " , fibonacci)








# 10
list = []
for item in range(1 , 11):
    list.append(item**2)

print(list)


            
        


   





# x = 10
# y = 20

# print(x%y)

# print(x>y)

# isRun = True
# isWalk = False

# print("logical operator")
# print(not isRun)

# take input in terminal

# x = input("Enter your first Number = ")
# y = input("Enter your second number = ")

# result  = int(x) + int(y)   #use int for convert string to variable
# print("The sum is" , result)


#functions
#space is metter when function is calling

# def greet():
#     print("name")
# greet()


# def name():
#     print("vijay")
# name()


#add two number functions

# def addNum(a,b):
#     result = int(a)+int(b)
#     print(result)
# addNum(10 , 25)

#return in functions

# def mul(a,b):
#     ans = int(a)*int(b)
#     return ans

# total = mul(25 , 5)
# print(total)


# built In function in Array 


#find the lenth of string
#len()
# text = "My name is khan"
# length = len(text)
# print(length)


#reverse the string

# def reverse_string(str):
#     bag=""
#     for char in str:
#         bag=char+ bag
#     return bag
    
# reversed = reverse_string("Python")
# print(reversed)



# use math

# import math

# result  = math.sqrt(15)
# print("Square root: " , result)



# my_module import export file

# def add(a,b):
#     print(int(a)+int(b))


# def greet(name):
#     print("Hello "+ name + " Welcome")

# greet("tarun")


