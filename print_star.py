print("solution 1")
i = 1
while i<=5:
    print('*'*i)
    i +=1
while (i-1)>=0:
    print('*'*(i-1))
    i -=1
print("solution 2")
n = 5
for i in range(n):
    for j in range(i):
        print("*",end='')
    print()
for i in range(n,0,-1):
    for j in range(i):
        print("*",end='')
    print()
