#Time - O(nlogn) || Space - O(1)
def twoNumberSum(array,targetSum):
    array.sort()
    start = 0
    end = len(array) - 1
    while(start < end):
        currSum = array[start] + array[end]
        if(currSum == targetSum):
            return [array[start],array[end]]
        elif(currSum < targetSum):
            start += 1
        else:
            end -= 1
    return []
        