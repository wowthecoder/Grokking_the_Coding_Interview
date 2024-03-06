from random import randint

# Time complexity: O(n^2)
# Space complexity: O(1)
# Worst when sorting a list in reverse order
# Best when input is nearly sorted 
# Or when the list is small, because it has smaller overhead compared to other methods
def insertion_sort(xs):
    for i in range(1, len(xs)):
        j = i
        while j > 0 and xs[j-1] > xs[j]:
            # swap
            xs[j-1], xs[j] = xs[j], xs[j-1]
            j -= 1
    return xs 

# Time complexity: O(n log n)
# Space complexity: O(n)
def merge(ls, rs):
        res = [] 
        l, r = 0, 0
        while l < len(ls) and r < len(rs):
            if ls[l] < rs[r]:
                res.append(ls[l])
                l += 1
            else:
                res.append(rs[r])
                r += 1 
        
        # Either ls or rs may have elements left
        if l != len(ls):
            res.extend(ls[l:])
        elif r != len(rs):
            res.extend(rs[r:])
        
        return res

def mergesort(xs):
    if len(xs) <= 1:
        return xs 
    
    half = len(xs) // 2
    left = xs[:half]
    right = xs[half:]
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

# Time Complexity (Worst case): O(n^2)
# Time Complexity (Average case): O(n log n)
# Space Complexity (arises from the recursive calls and the partitioning) : O(log n)
# Performs worst when list is already sorted
# Will exceed maximum recursion depth on large input sizes

# Splits xs[left..right] around xs[left] (first element in sublist)
def split(xs, left, right):
    pivot = xs[left]
    i = left + 1 
    j = right 
    # if xs[i] <= pivot, increment i (do the swap at the end)
    # if xs[i] > pivot, swap xs[j] and xs[i], and decrement j
    while i <= j:
        if xs[i] <= pivot: 
            i += 1
        else:
            xs[i], xs[j] = xs[j], xs[i]
            j -= 1
    # i = j + 1
    xs[left], xs[j] = xs[j], xs[left]
    return j


def quickSort(xs, left, right):
    if left > right or left < 0:
        return xs
    mid = split(xs, left, right)
    quickSort(xs, left, mid - 1)
    quickSort(xs, mid + 1, right)   
    return xs 

# Time complexity: O(n log n)
# Space complexity: O(1) (better than merge sort because we can sort in place)

# divide and conquer algorithm
def buildMaxHeap(xs, root, heapSize):
    left = 2*root 
    right = 2*root + 1 
    if left <= heapSize: 
        # root is not a leaf
        buildMaxHeap(xs, left, heapSize)
        if right <= heapSize: 
            buildMaxHeap(xs, right, heapSize)
    fixMaxHeap(xs, root, heapSize)

def fixMaxHeap(xs, root, heapSize):
    left = 2*root 
    right = 2*root + 1 
    if left <= heapSize:
        # root is not a leaf
        if left == heapSize or xs[left-1] > xs[right-1]:
            # no right subheap
            largerSubheap = left 
        else:
            largerSubheap = right 
        if xs[root-1] < xs[largerSubheap-1]:
            # swap
            xs[root-1], xs[largerSubheap-1] = xs[largerSubheap-1], xs[root-1]
            fixMaxHeap(xs, largerSubheap, heapSize)

def heapSort(xs):
    heapSize = len(xs)
    buildMaxHeap(xs, 1, heapSize)
    print("Heap: ", xs)
    # xs[0..heapSize-1] is the heap, xs[heapSize..len(xs)-1] is the sorted array
    while heapSize > 1:
        # delete the max element from heap and put it in the sorted array
        xs[0], xs[heapSize-1] = xs[heapSize-1], xs[0]
        heapSize -= 1 
        fixMaxHeap(xs, 1, heapSize)
    return xs

xs = []
if __name__ == "__main__":
    for i in range(20):
        xs.append(randint(0, 100))
    print("Original array: ", xs)
    ys = insertion_sort(xs)
    print("Insertion sort: ", ys)
    print("Correctly sorted? ", ys == sorted(xs))
    
    xs = []
    for i in range(20):
        xs.append(randint(0, 100))
    print("Original array: ", xs)
    ys = mergesort(xs)
    print("Merge sort: ", ys)
    print("Correctly sorted? ", ys == sorted(xs))

    xs = []
    for i in range(20):
        xs.append(randint(0, 100))
    print("Original array: ", xs)
    ys = quickSort(xs, 0, len(xs) - 1)
    print("Quick sort: ", ys)
    print("Correctly sorted? ", ys == sorted(xs))

    xs = []
    for i in range(20):
        xs.append(randint(0, 100))
    print("Original array: ", xs)
    ys = heapSort(xs)
    print("Heap sort: ", ys)
    print("Correctly sorted? ", ys == sorted(xs))