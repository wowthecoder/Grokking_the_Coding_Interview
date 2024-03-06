# As we said earlier, priority queues can be implemented as binary heaps. Let us recall
# the Min PQ as used for Prim’s algorithm:
# • Each item x of the queue has a priority key[x]
# • Items removed lowest key first.
# The operations are:
# • Q = PQcreate()
# • isEmpty(Q)
# • insert(Q, x)
# • getMin(Q)
# • deleteMin(Q)
# • decreaseKey(Q,x,newkey) — updates key[x] = newkey

class PriorityQueue:
    def __init__(self):
        self.arr = []