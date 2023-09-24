print("CALCULATOR")
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
i=1
while i<=5:
  print(" ")
  print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXIT")
  ch=int(input("Enter a choice:"))
  if ch==1:
    print(n1,"+",n2,"=", n1+n2)
  elif ch==2:
    print(n1,"-",n2,"=",n1-n2)
  elif ch==3:
    print(n1,"*",n2,"=",n1*n2)
  elif ch==4:
    print(n1,"/",n2,"=", n1/n2)
  else:
    break
