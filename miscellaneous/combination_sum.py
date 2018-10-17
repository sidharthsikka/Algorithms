def combination_sum(set, target):
    result = []
    count = 0
    for i in set:
        if i <= target:
            temp = []
            for j in result:
                if j+i <= target:
                    temp.append(j+i)
            result.extend(temp)
            result.append(i)
    for i in result:
        if i == target:
            count+=1
    return count

def combination_sum_paths(set, target):
    result = []

    def dfs(sum, i, curr):
        if sum == 0:
            result.append(curr)
            return
        elif sum > 0:
            for j in range(i,len(set)):
                dfs(sum-set[j], j, curr + [set[j]])
    
    dfs(target,0,[])
    return result

def combination_sum_paths_two(set, target):
    result = []
    set.sort()

    def dfs(sum, i, curr):
        if sum == 0 and curr not in result:
            result.append(curr)
        elif sum > 0:
            for j in range(i+1,len(set)):
                dfs(sum-set[j], j, curr + [set[j]])
    
    for i in range(0,len(set)):
        dfs(target-set[i],i,[set[i]])
    return result

def combination_sum_paths_three(set, target, k):
    result = []
    set.sort()

    def dfs(sum, i, curr):
        if len(curr) > k:
            return
        if sum == 0 and curr not in result:
            result.append(curr)
        elif sum > 0:
            for j in range(i+1,len(set)):
                dfs(sum-set[j], j, curr + [set[j]])
    
    for i in range(0,len(set)):
        dfs(target-set[i],i,[set[i]])
    return result

def main():
    print(combination_sum_paths_two([4,3,1,8],7))


main()