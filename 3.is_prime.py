def is_prime():
    n = int(input("Enter a number: "))
    if n <= 1:
        print("Not prime")
        return
    if n == 2:
        print("Prime")
        return
    i = 2
    while i * i <= n:
        if n % i == 0:
            print("Not Prime")
            return
        i += 1
    print("Prime")
