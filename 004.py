n = int(input())
num = list(map(int, input().strip().split()))

num.sort()

for i in range(0,n-1,2):
    if num[i] != num[i+1]:
        print(num[i])
        break
if num[n-1] != num[n-2]:
    print(num[n-1])