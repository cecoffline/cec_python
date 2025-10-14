n = int(input("Enter Number of N Terms: "))
if n <= 0:
    print("Fibonacci series for", n, "terms is not defined")
else:
    first = 0
    second = 1
    print("The first", n, "numbers in the Fibonacci series:")
    for i in range(n):
        if i == 0:
            print(first, end="")
        elif i == 1:
            print(",", second, end="")
        else:
            fib = first + second
            print(",", fib, end="")
            first = second
            second = fib
print()  
