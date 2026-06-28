array = [10, 3, 12, 1, 6, 4]

def quicksort(array):
    if len(array) < 2: 
        return array
    
    else: 
        pivo = array[0]

        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort(array))

def quicksortTwo(array):
    if len(array) < 2:
        return array
    
    else:   
        middle = int(len(array) / 2)
        pivo = array[middle]

        rest = array[:middle] + array[middle + 1:]

        menor = [i for i in rest if i < pivo]
        high = [i for i in rest if i > pivo]
    
    return quicksortTwo(menor) + [pivo] + quicksortTwo(high)

print(quicksortTwo(array))
    
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
