from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.maxHeap = [] # contains the smaller half
        self.minHeap = [] # contains the bigger half

    def addNum(self, num: int) -> None:
        if (len(self.maxHeap) == 0 or num <= -self.maxHeap[0]):
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        # balance the heaps
        if (len(self.maxHeap) > len(self.minHeap) + 1):
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif (len(self.minHeap) > len(self.maxHeap)):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        if (len(self.minHeap) == len(self.maxHeap)):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            return -self.maxHeap[0]