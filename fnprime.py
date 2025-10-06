num=int(input("Enter the value:"));
i=2
c=1
while c<=num:
 f=0
 j=2
  while j<=i//2:
   if (i%j)==0:
    f=1
     break
    j=j+1
    if f==0:
     print(i)
     k=k+1
    i=i+1
