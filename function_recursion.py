'''
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

print(factorial(int(input("enter a number : "))))
'''
'''
def factorial(n):
    result=1
    if n==0 or n==1:
        return 1
    for i in range(1,n+1):
        result=i*result
    return result

    
print(factorial(int(input("Enter a Number : "))
'''
'''
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

a=int(input("Enter a Number : "))
for i in range(a):
    print(fibonacci(i), end="")
'''
def sum_digit(n):
    if n==0:
        return 0
    return n%10+sum_digit(n//10)

print(sum_digit(245654))




















