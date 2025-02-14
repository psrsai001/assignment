def fact():
    n = int(input("Enter a number: "))
    res = n
    for i in range(2, n):
        res *= i
    print("Factorial:", res)
