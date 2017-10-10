import time

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def iterfibo(n):
    if n <= 1:
        return n
    else:
        a = [0,1]
        for i in range(n-1):
            a.append(a[i] + a[i+1])
        return a[n]

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
