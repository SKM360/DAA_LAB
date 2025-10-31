#Write a program to find factorial of a number using iterative and recursive method. Analyze time complexity. 

import time
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1) 
    
def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input("Enter a number: "))

s_time = time.time()
result = factorial_iterative(n)
e_time = time.time()

s_time2 = time.time()
result2 = factorial_recursive(n)
e_time2 = time.time()

print("Factorial of" ,n, f"IS {result:.5e} ")
print("Time taken (iterative): " ,e_time - s_time ,"seconds")

print(" Factorial of" ,n, f"IS {result2:.5e} " )
print("Time taken (recursive): " ,e_time2 - s_time2 ,"seconds")
