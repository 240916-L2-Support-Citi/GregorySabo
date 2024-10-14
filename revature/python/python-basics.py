#python basics demo

#this is a comment

#python uses indentation to define a code block

#variables and datatypes
	#we dont need to declare a variable type
age=25
name="Greg"
height= 5.8
is_associate = True

print("name", name)
print("age",age)
print("height",height)
print("is associate",is_associate)

user_name = input("enter your username: ")
print("hello " + user_name + "!")

# type conversion (casting!)
#if python takes out input they return it as a string
#tell the interpreter to convert our string to whichever datatype we want

user_age=input("Enter your age: ")
user_age_int=int(user_age)
print(f"in 5 years you will be {user_age_int +5}")


######################################
#+,-,*,/,%,**
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a ** b)

#######################################
#String and String manipulation
greeting = "string tesT"
print(greeting)
print(greeting.upper())
print(greeting.lower())
print(greeting[0:4])
print(greeting.replace("tesT","test")) 

#######################################
#boolean
is_raining = False
print("is it raining?", is_raining)

########################################
#comparison
#>,<,==(double becaue single equal is used to assign variable its value)
#>=,<=,is

x=5
y=10

print(x>y)
print(x is y)

#########################################
#list(arrays)
#LASTINFIRSTOFF
fruit = ["apple","mango","peach"]
print(fruit)
print(fruit[1])
fruit.append("orange")
print(fruit)
fruit.pop()
fruit.remove("apple")
print(fruit)

########################################
#range
	#often used in loops
number_list = list(range(100))
print(number_list)

#######################################
#tuple- a way to store multiple items in a single variable
#immutable - once created cannot be changed
coordinate = (10.0,20.1, "house of G")
print(coordinate)
print(coordinate[2])

#########################################
#sets
#unordered collection of UNIQUE elements
unique={1,2,2,2,2,2,2,3,4}
print(unique)
unique.add(5)
unique.add(6)
print(unique)

##########################################
#dictionary 
	#store key value pairs
	#keys must be unique, values can repeat
	#like dictionary, look up via its key
student = {
	"name": "Danny",
	"age": 25,
	"major": "Computer Science"
}
print(student)
print(student["age"])
student["age"]=26
print(student["age"])
student["gpa"]=3.9

#############################################
#none -null in python

result=None
print(result)

result = user_age
print(result)
