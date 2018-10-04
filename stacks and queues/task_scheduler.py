def leastInterval(tasks, n):
    map = {}
    for i in tasks:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    maxi = 0
    count = 0
    for i in map.keys():
        if(map[i] > maxi):
            maxi = map[i]
            count=1
        elif(map[i] == maxi):
            count+=1
    partCount = maxi - 1
    partLength = n - (count - 1)
    emptySlots = partCount * partLength
    availableTasks = len(tasks) - maxi * count
    idles = max(0, emptySlots - availableTasks)
    return idles + len(tasks)