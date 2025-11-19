#Print All the Values of Subarrays 
N = int(input())
arr = list(map(int, input().split()))
for start in range(N):
    for end in range(start, N):
        for i in range(start, end + 1):
            print(arr[i], end=" ")
        print()   
