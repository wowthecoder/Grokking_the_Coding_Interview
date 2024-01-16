class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            x = nums[i]
            # Array is sorted so we can't find any more triplets
            if (x > 0):
                break
            # We eliminate the same 1st element
            if (i > 0 and x == nums[i-1]):
                continue
            l, r = i+1, n-1
            while (l < r):
                y, z = nums[l], nums[r]
                sum3 = x + y + z
                if (sum3 > 0):
                    r -= 1
                elif (sum3 < 0):
                    l += 1
                else:
                    res.append([x, y, z])
                    # skip all the values that are same as current y and z
                    while (l < r and nums[l] == y):
                        l += 1
                        print(i, l, r)
                    while (l < r and nums[r] == z):
                        r -= 1
                        print(i, l, r)
        return res

                    