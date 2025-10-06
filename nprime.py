n=int(input("Enter how many prime numbers to display:")
count=0
num=2
while count<n:
 is_prime=true
 for i in range(2,num):
  if num%1==0:
    is_prime=False
    break
