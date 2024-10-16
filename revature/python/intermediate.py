import json
import re

#namespace and scope
global_string = "I am globally scoped variable."

#def my_function():
#	local_string = "I am globally scoped variable"
#	print(local_string)

#print(local_string)

def outer_function():
	outer_string = "I am enclosing scoped variable"
	print(outer_string)

	def inner_function():
		inner_string = "I am local scope scoped variable"
		print(inner_string)
	
	inner_function()

#print(inner_string) inner string dosnt exist here!

outer_function()

#######################################################

def exponent(x,y):
	result = x ** y
	return result

exp_return = exponent(10,10)
print(exp_return)

#######################################################
class Person:
	#class variable, every object will have the same species
	species = "Homo Sapiens"

	#construtor function called __init__
	def __init__(self,name_from_init,age_from_init):
		#instance variable. each perosn will have their own name, age
		self.name = name_from_init
		self.age = age_from_init

	#instance method
	def introduce(self):
		return f"My name is {self.name} and I am {self.age} years old"

	#static method. class function
	@staticmethod
	def talk():
		print("Talking from my static method that belongs to person")

#to call Person.talk()
Person.talk()

greg = Person("Gregory", 29)
print(greg.introduce())

#inheritance
class Employee(Person):
	def __init__(self, name, age, employee_id):
	
		super().__init__(name,age)
		self.employee_id = employee_id

	def introduce(self):
		return f"My name is {self.name} and my employee id is {self.employee_id}"

miguel = Employee("Miguel", 75, 123)

print(miguel.introduce())

##################################################
#lambda

numbers = [1,2,3,4,5,6,7,8,9,10]

#we want to take this list and make them all squared

square = list(map(lambda x: x**2,numbers))

print(square)

####################################################
#json in python
	#javascript object notation
	#transmit data through JSON
	#looks like python dictionary

pet_dict = {
	"name":"Penny",
	"age":10,
	"color":"white",
	#dictionary within a dictionary
	"toys":{
		"toy1": "ball",
		"toy2": "catnip"
	}
}
pet_json = json.dumps(pet_dict)

print(pet_dict)
print(pet_json)

#from object into json
greg_json = json.dumps(greg.__dict__)
print(greg_json)

#from json back into python dictionary
greg_dict = json.loads(greg_json)
print(greg_dict)

######################################################3
#regular expression - fast pattern matching
	#verify phone number matches correct format
	#verify email address is in proper

site_text = "contact us at info@mycompany.com or support@mywebsite.com"

#grab for email patterns
#we can use r - raw string literal (takes out things like \n \t etc....)
email_pattern = r"\b[A-Za-z0-9.]+@[A-Za-z0-9]+.[A-Za-z]{3}\b"

emails = re.findall(email_pattern, site_text)

print(f"emails found {emails}")
