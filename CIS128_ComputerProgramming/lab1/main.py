'''
arithmetic operations###


a = 10; b = 4;
print(a,b)


print(a+b)

print(a-b)


print(a*b)


print(a/b)


print(a/a)
#1.0 #Division operation always yields float output

print(a%b)


print(a//b)


print(a**b)



a=12; b=5;

a+=b
print(a)


a-=b
print(a)


a*=b
print(a)


a/=b
print(a)


a//=b
print(a)


a**=b
print(a)


a = int(a)
a%=b
print(a)


Arithmetic Expression: 2*3/3+5//2-1

Step 1: 6/3+5//2-1 #first multiplication
Step 2: 2.0+5//2-1 #division
Step 3: 2.0+2-1 #modulo division
Step 4: 4.0-1 #addition
Step 5: 3.0 #subtraction

'''


#Q1:please print "hello world" on the screen
# print("Hello Python World!")
print("hello world")

#Q2: Please print multiple lines of text on the screen
#print('''Today is Thursday
#This is the first python lecture
#I want to learn programming1''')

print('''Today is Thursday
This is the first python lecture
I want to learn programming1''')

#Q3: define two variables x and y, and x=3, y=4, z=x*y, please print the value of z on the screen.
x = 3
y = 4
z = x*y
print(z)

#Q4: please input a integer value for the variables x and y respectively, z= x*y, please print the value of z on the screen.
print('please input a value for x')
x = int(input('Please input an integer for x:'))
y = int(input('Please input an integer for y:'))
z = x*y
print(z)

#Q5: print more than one object:
print("hello","how are you")

#Q6: ask for a user's name and print it
print('Enter your name:')
x = input()
print('Hello, ' + x)

#Q7: Use the prompt parameter to write a message before the input:
x = input('Enter your name:')
print('Hello, ' + x)

#Q8: calculate an area of a circle
pi = 3.14159
radius = 2.2
# area of circle equation <- this is a comment
area = pi*(radius**2)
print(area)

#Q9: change the value of radius and print the area of the new circle
# change values of radius <- another comment
# use comments to help others understand what you are doing in code
radius = radius + 1
print(area)     # area doesn't change
area = pi*(radius**2)
print(area)

#Q10: practice comments
#############################
#### COMMENTING LINES #######
#############################
# to comment MANY lines at a time, highlight all of them then CTRL+1
# do CTRL+1 again to uncomment them
# try it on the next few lines below!

#area = pi*(radius**2)
#print(area)
#radius = radius + 1
#area = pi*(radius**2)
#print(area)

#############################
#### AUTOCOMPLETE #######
#############################
# Spyder can autocomplete names for you
# start typing a variable name defined in your program and hit tab 
# before you finish typing -- try it below

# define a variable
a_very_long_variable_name_dont_name_them_this_long_pls = 0

# below, start typing a_ve then hit tab... cool, right!
# use autocomplete to change the value of that variable to 1

# use autocomplete to write a line that prints the value of that long variable
# notice that Spyder also automatically adds the closed parentheses for you!