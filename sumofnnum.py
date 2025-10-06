n=int(input("Enter the number:"))
num=2
count=0
while (count<n):
	is_prime=True
	for i in range(2,num-1):
		if (num % i ==0):
			is_prime=False
			break
	if is_prime==True:
		print(num)
		count=count+1
	num=num+1	
