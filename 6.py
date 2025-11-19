#Contribution Technique – Sum of All Subarray Sums
N = int(input())
arr = list(map(int, input().split()))
total_sum = 0
for i in range(N):
    contribution = arr[i] * (i + 1) * (N - i)
    total_sum += contribution
print(total_sum)

