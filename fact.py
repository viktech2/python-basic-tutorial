n=input("Enter a number: ")
#print(n)
def factorial(n):
    if (n <= 1):
        return 1
    else:
        return (n*factorial(n-1))
    
#print(n)

#print("Result:", factorial(int(n)))
try:
    n = int(n)
    if(n > 0):
        print("Result:", factorial(n))
    else:
        print("-Ve number is not allowed")
except ValueError:
    print("Invalid input")

    
    

