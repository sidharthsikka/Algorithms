#N^2
def insertion_sort(arr):
    result = []
    for i in arr:
        index = 0
        for j in range(len(result)):
            if result[j] > i:
                index = j
                break
        result.insert(index,i)
    return result

def merge(A,B):
    temp = []
    index_a = 0
    index_b = 0
    while index_a < len(A) and index_b < len(B):
        if A[index_a] <= B[index_b]:
            temp.append(A[index_a])
            index_a += 1
        else:
            temp.append(B[index_b])
            index_b += 1
    while index_a < len(A):
        temp.append(A[index_a])
        index_a += 1
    while index_b < len(B):
        temp.append(B[index_b])
        index_b += 1
    return temp

#NlogN
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left,right)
    return arr

#NlogN
def quick_sort(arr, start, end):
    print(arr)
    print(start)
    print(end)
    if start < end:
        pivot = arr[end]
        pivot_index = end
        i = start
        while i < end:
            if arr[i] > pivot:
                temp = arr[i]
                del arr[i]
                pivot_index-=1
                arr.insert(end,temp)
            else:
                i+=1
            if pivot_index == 0:
                break
        quick_sort(arr, start, pivot_index-1)
        quick_sort(arr, pivot_index + 1, end)
    return arr

def heap_sort(arr):
    return

def main():
    print(quick_sort([4,50,2,100],0,3))

main()

