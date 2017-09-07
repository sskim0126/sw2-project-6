while True:
    num = int(input("Enter a number: "))
    if num == -1:
        break
    elif num < -1:
        continue
    else:
        def fac(num):
            if num == 1:
                return num
            elif num == 0:
                return 1
            else:
                return num*fac(num-1)
        print(num,"! =",fac(num))
