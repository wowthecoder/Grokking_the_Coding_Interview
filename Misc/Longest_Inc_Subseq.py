class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        len = 0
        for n in nums:
            if (len == 0 or n > nums[len-1]): # extend
                nums[len] = n
                len += 1
            else: # replace
                # find smallest element >= current n in the prev elements
                idx = bisect_left(nums[:len], n)
                print(len, nums[len], idx)
                nums[idx] = n
        return len