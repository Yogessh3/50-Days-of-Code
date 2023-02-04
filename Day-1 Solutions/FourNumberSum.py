def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            currSum = array[i] + array[j]
            currDiff = targetSum - currSum
            if currDiff in allPairSums:
                for pair in allPairSums[currDiff]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(i):
            currSum = array[i] + array[k]
            if currSum in allPairSums:
                allPairSums[currSum].append([array[i], array[k]])
            else:
                allPairSums[currSum] = [[array[i], array[k]]]
    return quadruplets
