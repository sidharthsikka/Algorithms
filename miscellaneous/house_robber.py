def rob_recursive(nums, i):
    if i > len(nums)-1:
        return 0
    return max(nums[i] + rob_recursive(nums, i+2), rob_recursive(nums, i+1))

def rob_iterative(nums):
    if len(nums) == 0:
        return 0
    memo = [0, nums[0]]
    for i in range(1,len(nums)):
        memo.append(max(nums[i] + memo[i-1], memo[i]))
    return memo[len(nums)]

def rob_2_recursive(nums, i,houses):
    if i > len(nums) - 1:
        return 0
    if (i+1) % len(nums) == 0 and 0 in houses:
        return 0
    return max(nums[i] + rob_2_recursive(nums, i+2, houses + [i]), rob_2_recursive(nums, i+1, houses))

def rob_2_iterative(nums):
    if len(nums) == 1:
        return nums[0]
    return max(rob_iterative(nums[1:]), rob_iterative(nums[:len(nums)-1]))




def main():
    print(rob_2_iterative([1,1,1,2]))    

main()