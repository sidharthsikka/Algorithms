def unique(arr):
    map = {}
    for i in arr:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    for i in arr:
        if map.get(i) == 1:
            return i