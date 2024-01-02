class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = [intervals.pop(0)]
        while intervals:
            a = res.pop()
            b = intervals.pop(0)
            # b.start <= a.end
            if (b[0] <= a[1]):
                res.append([a[0], max(a[1], b[1])])
            else:
                res.append(a)
                res.append(b)
        return res