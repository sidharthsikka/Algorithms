from collections import deque

def sliding_window_max(nums,k):
    result = []
    q = deque()

    for i in range(len(nums)):
        while q and nums[q[-1]] < nums[i]:
            q.pop()

        q.append(i)

        if q[0] <= i-k:
            q.popleft()

        if i >= k-1:
            result.append(nums[q[0]])

    return result