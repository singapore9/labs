import sys
filename = 'L1n2.txt'

def getArr(line):
    return list(map(int, line.split()))

def sepIndex(arr, first, last):
    base = arr[first]
    l = first + 1
    r = last
    while True:
        while l <= r and arr[l]<=base:
            l += 1
        while l <= r and arr[r]>=base:
            r -= 1
        if l>r:
            break
        else:
            arr[l], arr[r] = arr[r], arr[l]
        arr[first], arr[r] = arr[r], arr[first]
    return r

def quickFunc(arr, first, last):
    if first<last:
        sep = sepIndex(arr, first, last)
        quickFunc(arr, first, sep - 1)
        quickFunc(arr, sep + 1, last)
    
def quickSort(line):
    arr = getArr(line)
    quickFunc(arr, 0, len(arr)-1)
    return arr

#------------------------
def mergeFunc(arr):
    if len(arr)>1:
        mid = len(arr)//2
        p1 = arr[:mid]
        p2 = arr[mid:]
        mergeFunc(p1)
        mergeFunc(p2)
        i1, i2, i = 0, 0, 0
        while (i1<len(p1))&(i2<len(p2)):
            if p1[i1]<p2[i2]:
                arr[i]=p1[i1]
                i1 += 1
            else:
                arr[i]=p2[i2]
                i2 += 1
            i += 1
        while i1 < len(p1):
            arr[i] = p1[i1]
            i, i1 = i+1, i1+1
        while i2 < len(p2):
            arr[i] = p2[i2]
            i, i2 = i+1, i2+1
        

def mergeSort(line):
    arr = getArr(line)
    mergeFunc(arr)
    return arr

#--------------------------
def radixSort(line):
    arr = list(map(str, getArr(line)))
    mxLen = max(list(map(len, arr)))
    for i in range(len(arr)):
        arr[i] = arr[i].zfill(4)
    positive = [number for number in arr if not number.count('-')]
    negative = [number[1:] for number in arr if number.count('-')]
    positive = radixFunc(positive)
    negative = ['-'+number for number in radixFunc(negative)]
    negative.reverse()
    ans = negative + positive
    ans = list(map(int, ans))
    return ans

def radixFunc(arr):
    for curRad in range(len(arr[0]) - 1, -1, -1):
        _range = []
        for x in range(10):
            _range.append([])
        for i in range(len(arr)):
            _range[int(arr[i][curRad])].append(arr[i])
        arr = []
        for i in range(10):
            if _range[i]:
                for j in range(len(_range[i])):
                    arr.append(_range[i][j])
    return arr  

def main(line = open(filename, 'r').read()):
    #import random
    #line = ''
    #for i in range(12):
    #    line += ' ' + str(random.randrange(-10, 10))
    print('Input data:', getArr(line))
    print('QuickSort: ', quickSort(line))
    print('MergeSort: ', mergeSort(line))
    print('RadixSort: ', radixSort(line))

if __name__ == '__main__':
    try:
        if '-f' in sys.argv:
            filename = sys.argv[sys.argv.index('-f') + 1]
    except:
        filename = 'L1n2.txt'
    main()
with open(filename, 'r') as f:
    line = f.read()
