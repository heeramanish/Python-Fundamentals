# variable and data types
# string, Numbers , TRUE/FALSE
charater_name = "John"
charater_age = "35"

print("There once was a man named " + charater_name + " , ")
print("he was 35 years old.")


#working with strings

phrase = "Monash University"
print(phrase.lower()) #lowercase
print(phrase.upper()) #uppercase
print(phrase.isupper()) #checking if it is upper case
print(len(phrase)) #length function
print(phrase[0]) #index 0 which is M
print(phrase.index("s"))  #index of s, first s from 0 index
print(phrase.replace("Monash", "Deakin"))


# working with numbers

from math import *

print(3*4+5)
my_num  = 9
print(abs(my_num))
print(pow(my_num,2))  # 9^2
print(round(7.88))
print(floor(3.7))
print(ceil(3.1))
print(sqrt(49))

#Getting input from user

name = input("Enter your name: ")
Age = input("Enter your Age: ")

print("Hello " + name + " you are " + Age)


#building basic calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1+num2
print(result)  #by deafult python gonna give us putput a string

result1= int(num1) + int(num2)
print(result1)


######## LIST ##########

friends = ["kevin", "karen", "Tom"]
print(friends)

lucky_number = [4,8,16,23,42]
friends.extend(lucky_number) #2 lists joined together`
print(friends)

friends.append("creed") #adding additional element in the list friend
print(friends)
friends.insert(1, kelly) #inserted kelly at index 1
friends.remove("Tom") #removing tom from list
friends.pop() # this will remove last item from the list
friends.sort() #sorting the list increasing order or alphabetical order in this case
friends2 = friends.copy() #copied friends list in friends2

####### Tuples #######
## container where we can store various values ###
## tuples are immutable i.e. cannot be modified once created ##
coordinates = (4,5)
# coordinates[1] = 10 #not possible cos immutable
print(coordinates[1]) ## output is 5


#######################
###### Functions ######
#def a keyword for funnction

def sayhi():
    print("Hi")

sayhi()      #calling function then only it works

def say_hi(name_1):
    print("Hi" + name_1)

say_hi(Mikey)








