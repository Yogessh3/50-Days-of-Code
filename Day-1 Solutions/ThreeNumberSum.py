#O(N^2) Time / O(N) Space
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for idx in range(len(array) - 2):
        left = idx + 1
        right = len(array) - 1
        while(left < right):
            currSum = array[idx] + array[left] + array[right]
            if(currSum == targetSum):
                triplets.append([array[idx], array[left], array[right]])
                left += 1
                right -= 1
            elif(currSum < targetSum):
                left += 1
            elif(currSum > targetSum):
                right -= 1
    return triplets  