#Kadane’s Algorithm 
N = int(input())
nums = list(map(int, input().split()))
max_ending_here = nums[0]
max_so_far = nums[0]
for i in range(1, N):
    max_ending_here = max(nums[i], max_ending_here + nums[i])
    max_so_far = max(max_so_far, max_ending_here)
print(max_so_far)
