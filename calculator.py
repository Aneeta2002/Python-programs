def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
def mod(a,b):
	return a%b
def power(a,b):
	return a**b
def calc(a, operator ,b):
	if operator=="+":
		return add(a,b)
	elif operator=="-":
		return sub(a,b)
	elif operator=="*":
		return mul(a,b)
	elif operator=="/":
		return div(a,b)
	elif operator=="%":
		return mod(a,b)
	elif operator=="**":
		return power(a,b)
	else:
		print("Invalid")
a=float(input("Enter the first number="))
operator=input("Enter the operator=")
b=float(input("Enter the second number="))
result=calc(a,operator,b)
print("Result=",result)
