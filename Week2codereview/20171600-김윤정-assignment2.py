A=int(input("Enter a number:"))
while A != -1:
    output=1
    for i in range(A):
        output *= (i+1)
    print("%d! =" %A, output)
    A = int(input("Enter a number:"))
