num=int(input("enter the length of fibonacci series"))

n1 = 0
n2 = 1
print("the fibonacci series of length", num)
print(n1, n2 , end=" ")
for i in range(2,num):
        n3 = n1+ n2
        print( n3, end=" ")
        n1 = n2
        n2 = n3
print()
