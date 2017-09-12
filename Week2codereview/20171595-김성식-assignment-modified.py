def fac(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

while True:
    try:
        n = int(input("Enter a number: "))
    except:
        print("Error")
    else:
        if n >= 0:
            print(fac(n))
        elif n == -1:
            break
        else:
            print("Enter 0 or natural numbers")
