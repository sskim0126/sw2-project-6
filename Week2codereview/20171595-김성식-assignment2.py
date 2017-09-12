n = input("Enter a number: ")

try:
    n = int(n)
except:
    print("Error")
else:
    while n >= 0:
        if n >= 1:
            result = 1
            for i in range(1, n+1):
                result = result * i
            print(result)
        else:
            print(1)

        n = input("Enter a number: ")
        if n == -1:
            break
        try:
            n = int(n)
        except:
            print("Error")
            break

