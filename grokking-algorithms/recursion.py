def lookForKey(mainBox):
    stack = [mainBox]

    while stack:
        box = stack.pop()

        for item in box:
            if item == "key":
                print("Found the key!")
                return
            
            elif isinstance(item, list):
                stack.append(item)

mainBox = [
    ["book", "clothes"],
    ["documents", "key"], 
    ["pen"]
]

def recursiveLookForKey(mainBox):
    for item in mainBox:
        if isinstance(item, list):
            recursiveLookForKey(item)
    
        elif item == "key":
            print("Found the key!")
            return
            

lookForKey(mainBox)
recursiveLookForKey(mainBox)

class Item: 
    def __init__(self, itemType, content=None):
        self.itemType = itemType
        self.content = content
    
    def isBox(self):
        return self.itemType == "box"

    def isKey(self):
        return self.itemType == "key"
    

def lookForKeyOOP(mainBox):
    stack = [mainBox]

    while stack:
        currentBox = stack.pop()

        for item in currentBox.content:
            if item.isBox():
                stack.append(item)
            elif item.isKey():
                print("Found the key!")

key = Item("key")
smallBox = Item("box", content = [key])
bigBox = Item("box", content=[smallBox])

lookForKeyOOP(bigBox)

def fatorial(num):
    if num >= 0 and num <= 1:
        return 1
    
    else:
        return num * fatorial(num-1)

print(fatorial(5))

def sum(array):
    if len(array) == 0:
        return 0
    
    x = array.pop()
    x += sum(array)
    return x


array = [2, 4, 6]
result = sum(array)

print(result)

array = [2, 4, 6]

def countNumbers(array):
    if len(array) == 0:
        return 0
    
    array.pop()
    x = 1 + countNumbers(array)
    return x

result = countNumbers(array)
print(result)

array = [2, 10, 6, 4, 1, 9]

def sumTwo(array):
    if array == []:
        return 0
    
    return array[0] + sumTwo(array[1:])

print(sumTwo(array))

def count(array):
    if array == []:
        return 0
    
    return 1 + count(array[1:])

print(count(array))

def high(array, elem):
    if array == []:
        return elem
    
    if elem < array[0]:
        return high(array[1:], array[0])
    
    return high(array[1:], elem)


print(high(array, 0))

def max(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    
    subMax = max(array[1:])

    return array[0] if array[0] > subMax else subMax

print(max(array))

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
        
        menor = [i for i in array[1:] if i <= array[middle]]
        high = [i for i in array[1:] if i > array[middle]]
    
    return quicksort(menor) + [array[middle-1]] + quicksort(high)

print(quicksortTwo(array))
    
