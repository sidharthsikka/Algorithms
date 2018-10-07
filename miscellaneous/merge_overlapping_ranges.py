from operator import itemgetter

# input is a list of tuples indicating range of numbers
def merge_overlapping_ranges(list):
    if len(list) == 0:
        return []
    sorted_list = sorted(list, key = itemgetter(0))
    stack = [sorted_list[0]]
    for i in sorted_list:
        temp = stack[-1]
        if i[0] >= temp[0] and i[0] <= temp[1] or i[1] >= temp[0] and i[1] <= temp[1]:
            stack.pop()
            if i[0] <= temp[0]:
                if i[1] >= temp[1]:
                    stack.append(i[0],i[1])
                else:
                    stack.append(i[0],temp[1])
            else:
                if i[1] >= temp[1]:
                    stack.append(temp[0],i[1])
                else:
                    stack.append(temp[0],temp[1])
        else:
            stack.append(i)
    return stack