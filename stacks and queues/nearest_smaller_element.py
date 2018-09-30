def nearest_smaller_element(arr):
    smallest_number = 1e10
    stack = []
    result = []
    for i in arr:
        if i <= smallest_number:
            stack = [i]
            smallest_number = i
            result.append(-1)
        else:
            while stack:
                temp = stack.pop()
                if temp < i:
                    stack.append(temp)
                    stack.append(i)
                    result.append(temp)
                    break
    return result

def main():
    print(nearest_smaller_element([5,4,3,2,1]))


main()
    