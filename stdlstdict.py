std={}
n=int(input("Enter the number of students:"))
for i in range(n):
	name=input("\nEnter student name:")
	age=int(input("\nEnter the age:"))
	grade=input("\nEnter the grade:")
	std[name]=(age,grade)
print("\nStudent records:")
for name,details in std.items():
	print("Name:",name,"|Age:",str(details[0]),"|Grade:",grade)
