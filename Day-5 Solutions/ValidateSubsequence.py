def validateSubsequence(array, sequence):
    arrayIdx = 0
    sequenceIdx = 0
    while arrayIdx < len(array) and sequenceIdx < len(sequence):
        if(array[arrayIdx] == sequence[sequenceIdx]):
            sequenceIdx += 1
        arrayIdx += 1
    return sequenceIdx == len(sequence)
