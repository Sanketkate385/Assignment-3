# Task 1:

def Factorial(n):

    if n < 2:
        return 1
    else:
        return n * (Factorial(n-1))

n = int(input("Enter the number: "))
result = Factorial(n)
print("The Factorial of", n , "is" ,result)