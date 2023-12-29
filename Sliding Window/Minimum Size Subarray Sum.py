# Initial approach
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum, minLen, end = 0, 0, 0
        # Find the subarray starting from first element
        for j in range(len(nums)):
            currSum += nums[j]
            if currSum >= target:
                minLen = j + 1    
                end = j           
                break
        if minLen == 0:
            return 0
        currLen = minLen
        # Find the subarrays starting from 2nd,3rd,4th... element
        for i in range(len(nums)-1):
            currSum -= nums[i]
            while currSum < target and end < len(nums) - 1:
                end += 1
                currSum += nums[end]
            if currSum >= target:
                currLen = end - (i + 1) + 1
                minLen = min(currLen, minLen)
        return minLen