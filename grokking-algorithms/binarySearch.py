def binanrySearch(list, item):
    low = 0
    high = len(list) - 1

    while (low <= high):
        middle = (low + high) // 2
        shot = list[middle]

        if (shot == item):
            return middle
        
        elif (shot > item):
            high = middle - 1
        
        elif (shot < item):
            low = middle + 1
    
    return None

list = [1, 4, 6, 8, 11, 14, 16, 19]
target = 16

position = binanrySearch(list, target)

print("Position: ", position)