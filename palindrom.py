def  is_palindrome(n):
	n_str = str(n)
	n_rev	= n_str[::-1]
	return n_str == n_rev
num=int(input("Enter the number:"))
result=is_palindrome(num)
if result:
	print("This number is palindrome")
else:
	print("This number is not palindrome")
