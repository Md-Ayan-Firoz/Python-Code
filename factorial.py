def fact():
    if n<0:
        print("Factorial Does Not Exist")
    elif n==0:
        print("The Factorial Of Zero is 1")
    else:
        fact = 1
        for i in range(1,n+1):
                fact=fact*i
        print("Factorial of n is: ",fact)

n=int(input("Enter The Number: "))
fact()
