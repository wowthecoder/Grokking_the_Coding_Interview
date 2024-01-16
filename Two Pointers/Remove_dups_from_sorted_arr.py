class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq = 1
        n = len(nums)
        for curr in range(1, n):
            if (nums[curr] != nums[curr-1]):
                nums[uniq] = nums[curr]
                uniq += 1
        return uniq
