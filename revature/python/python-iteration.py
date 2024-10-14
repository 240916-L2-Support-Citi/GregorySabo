#iteration and conditionals

#for loop
	#iterate over a list or range of number
fruit = ["apple","banana","mango"]

for fruits in fruit:
	print(fruits)

for i in range(3,10):
	print(i)

##############################################
#if else
	#make desicions based on condition
student= {
	"name":"greg",
	"major":"Computer Science"
}

if student["major"] == "Computer Science":
	print("coding/coding")
else:
	print("writing/reading")

###################################################3
#while

count=10

while count > 0:
	print(count)
	count -= 1

#infinite
while True:
	userfeedback = input("enter 'exit' to stop loop!")
	if userfeedback == "exit":
		print("Exiting loop")
		break

#rangel
for number in range(1,11):
	if(number%2==0):
		print(f"{number} is even")
	else:
		print(f"{number} is odd")
