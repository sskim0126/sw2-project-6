#팩토리얼을 ->재귀함수
n = int(input())
def factorial(n):
	if (n <= 1):
		return 1

	return factorial(n-1) * n

print(factorial(n))

#팩토리얼 ->조합
def factorial(n):
	if (n <= 1):
		return 1

	return factorial(n-1) * n


if __name__ == '__main__':
	n = int(input())
	r = int(input())
	result = factorial(n) / (factorial(r) * factorial(n-r))

	print(result)

#재귀함수->조합

n = int(input("n= "))
r = int(input("r= "))
def combination(n,r):
    def factorial(n):
        if (n <= 1):
            return 1
        return factorial(n - 1) * n
    result = factorial(n) / (factorial(r) * factorial(n-r))
    return result
    return combination(n-1,r-1) + combination(n-1,r)
print (combination(n,r))
