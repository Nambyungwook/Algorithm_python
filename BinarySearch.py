def binarySearch(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

testList = [1,3,5,6,7,8,10]
 
print(binarySearch(testList, 3))
print(binarySearch(testList, -1))