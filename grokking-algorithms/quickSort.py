array = [10, 3, 12, 1, 6, 4]

def lowElement(array):
    smallest = 0

    for i in range(len(array)):
        if array[i] < array[smallest]:
            smallest = i
    
    item = array.pop(smallest)

    return item

def sort(array): 
    newArray = []
    
    while(array):
        item = lowElement(array)
        newArray.append(item)

    return newArray

def selectSort(array): 
    size = len(array)

    for i in range(size - 1):
        smallestIndex = i

        for j in range(i + 1, size):
            if array[j] < array[smallestIndex]:
                smallestIndex = j

        array[i], array[smallestIndex] = array[smallestIndex], array[i] 

    return array

print(selectSort(array))
