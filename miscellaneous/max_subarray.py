'''
* This method goes through each array passed through it and keeps track of the maximum sum of contagious numbers it has seen so far and to account for negative integers being present
it also takes note of the current sum resetting when we have reached below zero as any sum after that will always be bigger

* Possible cases to take note off would be if the array length is 0 then i assume we return the max sum as 0 since it is not stated in the question, a set with all negative numbers will
have a answer of a single number, an array with one number wont have a comma to split on
'''

def max_sub_array(arr):
    sizeOfArray = len(arr)
    if(sizeOfArray == 0):
        return 0
    currMax = 0
    result = -99999
    for i in range(sizeOfArray):
        currMax += arr[i]
        if(result < currMax):
            result = currMax
        if(currMax < 0):
            currMax = 0
    return result

def main():
    print(max_sub_array([1,2,3]))

main()