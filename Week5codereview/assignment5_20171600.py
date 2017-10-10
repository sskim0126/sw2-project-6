import time

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


def iterfibo(n):
    list = [0,1]
    for i in range(2, n+1):
        list.append(list[i-1]+list[i-2])
    return list[-1]


while True:
    try:
        nbr = int(input("Enter a number: "))
        if nbr == -1:
            break
        elif nbr < -1:
            raise ValueError
    except ValueError:
         print("0이상의 정수만 입력하세요")
    else:
         ts = time.time()
         fibonumber = iterfibo(nbr)
         ts = time.time() - ts
         print("IterFibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
         ts = time.time()
         fibonumber = fibo(nbr)
         ts = time.time() - ts
         print("Fibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))

