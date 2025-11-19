# Print Sum of Every Single Subarray
N = int(input())
arr = list(map(int, input().split()))
for start in range(N):
    current_sum = 0
    for end in range(start, N):
        current_sum += arr[end]  
        print(current_sum)        
