def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    while(left < right):
        if(array[left] == toMove):
            if(array[right] != toMove):
                array[left], array[right] = array[right], array[left]
                left += 1
            else:
                right -= 1
        else:
            left += 1
    return array
