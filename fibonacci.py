# 7. Generate a Fibonacci sequence up to n terms.
def fib():
    n = int(input("Enter a number: "))
    a = 0
    b = 1

    if n == 1:
        print(a)
        return
    if n == 2:
        print(a, b)
        return
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
