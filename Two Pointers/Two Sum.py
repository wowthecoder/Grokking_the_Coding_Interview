class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a sorted 2d array with the values and original indices
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        l, r = 0, len(nums) - 1
        while (l <= r):
            x = sorted_nums[l][1] + sorted_nums[r][1]
            if (x == target):
                return [sorted_nums[l][0], sorted_nums[r][0]]
            elif (x < target):
                l += 1
            else:
                r -= 1
        return [-1, -1]
