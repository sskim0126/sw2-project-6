while True:
    try:
        n = int(input("Enter a number: "))
    except:
        print("Error")
        continue
    if n == -1:
        break
    elif n < -1:
        print("Error")
    else:
        def fac(n):
            a = 1
            for i in range(1, n + 1):
                a *= i
            return a
        print("%d! = " %n, fac(n))