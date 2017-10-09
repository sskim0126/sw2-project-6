#재귀함수로 구현한 피보나치 수열
def fibo(num):
    if num <= 1:
        return num
    return fibo(num - 1) + fibo(num - 2)

#반복적으로 구현한 피보나치 수열
def iterfibo(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        fibolist = [1, 1]
        count = 0 #fibolist 교체 횟수
        while count + 2 < num:
            constant = 0
            for i in range(0,len(fibolist)):
                constant += fibolist[i]
            count += 1
            del fibolist[0]
            fibolist.append(constant)
        return fibolist[1]

#시간비교
import time
while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() -ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
