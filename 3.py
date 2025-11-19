#Find the Sum of Elements in a Given Subarray
N = int(input())
arr = list(map(int, input().split()))
L, R = map(int, input().split())
L -= 1
R -= 1
result = sum(arr[L:R+1])
print(result)
