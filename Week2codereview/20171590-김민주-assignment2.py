n = int(input("Enter a number: "))

while n < -1:
    n = int(input("Enter a number: "))
    while n > -1:
        def fac(n):
            a = 1
            for i in range(1, n + 1):
                a *= i
            return a
        print(n, " ! = ", fac(n))
        n = int(input("Enter a number: "))
    if n == -1:
        break