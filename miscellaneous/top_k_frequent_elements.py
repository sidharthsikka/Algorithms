def top_k_frequent_elements(nums,k):
    map1 = {}
    map2 = {}
    res  = []
    
    for num in nums:
        if num in map1:
            map1[num] += 1
        else:
            map1[num] = 1

    for key, value in map1.items():
        if value in map2:
            map2[value].append(key)
        else:
            map2[value] = [key]
            
    for freq in range(len(nums), 0, -1):
        if freq in map2:
            res += map2[freq]
            
    return res[:k]