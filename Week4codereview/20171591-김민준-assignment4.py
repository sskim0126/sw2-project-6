#팩토리얼 재귀함수코드
while True:
    num = input("Enter a number : ")
    try:
        num = int(num)
        if num < -1:
            raise ValueError
        elif num == -1:
            break
    except ValueError:
        print("0이상의 정수만 입력해주세요")

    else:
        def factorial(num):
            if 0 <= num <= 1:
                return 1
            else:
                return num * factorial(num-1)
        print("%d! =" %num,factorial(num))


#팩토리얼로 구한 조합코드
while True:
    n = input("Enter a number: ")
    r = input("Enter a number: ")
    try:
        n = int(n)
        r = int(r)
        if n < -1 or r < -1 :
            raise ValueError
        elif n < r: # n >= r 이어야하는 예외처리
            print("n은 r보다 반드시 크거나 같아야 합니다.")
            continue
    except ValueError:
        print("0이상의 정수만 입력해주세요")
    except: # 문자가 들어오는 경우 예외처리
        continue
    else:
        def fac(a):
            if 0 <= a <= 1:
                return 1
            else:
                return a * fac(a-1)
        print("%dC%d = " %(n,r) , fac(n)//fac(n-r)//fac(r))

#조합 재귀함수코드
while True:
    n = input("Enter a number: ")
    r = input("Enter a number: ")
    try:
        n = int(n)
        r = int(r)
        if n < -1 or r < -1:
            raise ValueError
        elif n < r: #n >= r 이어야하는 예외처리
            print("n은 r보다 반드시 크거나 같아야 합니다.")
            continue
    except ValueError:
        print("0이상의 정수만 입력해주세요")
        continue
    except: #문자가 들어오는 경우 예외처리
        continue
    else:
        def Combination(n,r): 
            if r == 0:
                return 1
            else:
                decision = n / r
                return decision * Combination(n-1, r-1)
        print("%dC%d = " %(n,r) , int(Combination(n,r)))
        break




