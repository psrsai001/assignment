def swap():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print("before:", "a:", a, "b:", b)
    a, b = b, a
    print("afer:", "a:", a, "b:", b)
