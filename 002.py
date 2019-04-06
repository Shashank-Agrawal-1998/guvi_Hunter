n = int(input())
num = list(map(int, input().strip().split()))

num = sorted(num, reverse=1)

largest_num = 0

for i in num:
    largest_num = (largest_num * 10) + i
    
print(largest_num)
    