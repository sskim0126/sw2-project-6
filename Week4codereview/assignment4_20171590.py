#팩토리얼을 재귀함수로 코드짜기

n = int(input("n = "))

def fac(n):
    if n <= 1:
        return 1
    return fac(n-1) * n

print(fac(n))


#조합을 팩토리얼로 코드 짜기

def fac(n):
    if n <= 1:
        return 1
    return fac(n-1) * n

if __name__ == '__main__':
    n = int(input("n = "))
    r = int(input("r = "))

    result = fac(n) / (fac(r) * fac(n-r))
    print(int(result))


#조합을 재귀함수로 코드 짜기

n = int(input("n = "))
r = int(input("r = "))

def combi(n,r):
    if (n == r or r == 0):
        return 1
    else:
        return combi(n-1, r-1) + combi(n-1, r)

print(combi(n,r))