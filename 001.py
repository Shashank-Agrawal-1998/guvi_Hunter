n = int(input())
n_numbers = list(map(int, input().strip().split()))
n_numbers.sort()
repeated_numbers = set()

for i in range(n-1):
    if n_numbers[i] == n_numbers[i+1]:
        repeated_numbers.add(n_numbers[i])

repeated_numbers = list(repeated_numbers)

if len(repeated_numbers)==0:
    print("unique")
else:
    for i in repeated_numbers:
        print(i, end=" ")