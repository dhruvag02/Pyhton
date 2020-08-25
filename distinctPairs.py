def isNotEmpty(a):
    if len(a) == 0:
        return True
    else:
        return False


def  binarySearch(a, value):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high)//2
        if a[mid] < value:
            low = mid+1
        elif a[mid] > value:
            high = mid-1
        else:
            return True
    return False


def distinctPairs(n, a, k):
    if n == 0:
        return 0
    a.sort()
    print(a)
    count = 0
    i = 0
    while (i < n) or (isNotEmpty(a)):
        i = i+1
        try:
            item = a[0]
        except:
            return count
        value = k-item
        if binarySearch(a, value):
            a.remove(value)
            a.remove(item)
            print(a)
            count = count + 1
        else:
            continue
    return count


n = 6
a = [1, 18, 13, 6, 10, 9]
k = 19
pairs = distinctPairs(n, a, k)
print(pairs)
