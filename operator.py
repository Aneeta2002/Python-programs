a=int(input("Enter the first element:"))
b=int(input("Enter the second element:"))
c=input("Enter the operator:")
if c ==   '+':
	print("Result=",a+b)
elif c ==  '-':
	print("Result=",a-b)
elif c ==  '*':
	print("Result=",a*b)
elif c ==  '/':
	print("Result=",a/b)
elif c ==  '//':
	print("Result=",a//b)
elif c ==  '%':
	print("Result=",a%b)
elif c ==  '**':
	print("Result=",a**b)
else:
	print("Invalid")
