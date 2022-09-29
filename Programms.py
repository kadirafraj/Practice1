n = int(input("please give first number: "))
while n>0:
    dig=n%10
    if dig!=0 and dig!=1:
        print("Given Number is not a Binary Number")
        break
    n=n//10
    if n==0:
        print("Given Number is Binary Number")