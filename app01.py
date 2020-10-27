# Mad lib game
color = input("Enter a color")
plural_noun = input("Enter a plurar noun")
celebrity = input("Enter a celeb")

print("Roses are "+ color)
print(plural_noun + " are blue")
print("I love "+ celebrity)


# function returning a number

def cube(num):
    print (num*num*num)

cube(3)

# OR return function

def sqr(num1):
    return num1*num1

print(sqr(4))


#####################
###### IF ELSE ######
#####################

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a tall or Male") #output
else:
    print("Not a male or tall!")


if is_tall and is_male:
    print("You are a tall guy") #output
elif is_male and not(is_tall):
    print("you are short guy")
else:
    print("neither tall nor a male")





