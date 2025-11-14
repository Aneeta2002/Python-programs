a=int(input("Enter the number of name:"))
names=[ ]
for i in range(a):
	name=input("Enter name:")
	names.append(name)
names.sort()
print("\n Names in alphabetical order:")
for name in names:
	print(name)
