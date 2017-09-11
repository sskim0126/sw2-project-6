while True:
    try:
        A = int(input("Enter a number:"))
    except:
        print("예외처리됨")
        continue

    output = 1
    if A == -1:
        break
    elif A < -1:
        print("Error")
    else:
        for i in range(A):
            output *= (i+1)
        print("%d! =" %A, output)
