n = int(input())
num = list(map(int, input().strip().split()))

arr = []

for i in range(n):
    if i == num[i]:
        arr.append(i)
        
arr.sort()
if len(arr)==0:
    print('-1')
else:
    for i in arr:
        print(i, end=" ")