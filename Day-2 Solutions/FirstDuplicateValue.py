#Time - O(N^2) || Space - O(1)
def firstDuplicateValue(array):
    minimumIndex = len(array)
    for i in range(len(array)):
        value = array[i]
        for j in range(i+1,len(array)):
            valueToCompare = array[j]
            if(value == valueToCompare):
                minimumIndex = min(minimumIndex,j)
                break
    return -1 if minimumIndex == len(array) else array[minimumIndex]

#Time - O(N) || Space - O(N)
def firstDuplicateValue(array):
    visitedValues = set();
    for number in array:
        if number in visitedValues:
            return number
        visitedValues.add(number)
    return -1

#Time - O(N) || Space - O(1)
def firstDuplicateValue(array):
    for idx in range(len(array)):
        currNumber = abs(array[idx])
        validationIdx = currNumber - 1
        if(array[validationIdx] < 0):
            return currNumber
        array[validationIdx] *= -1
    return -1