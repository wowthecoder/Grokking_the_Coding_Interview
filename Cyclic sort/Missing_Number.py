class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = -1
        # cycle sort
        i = 0
        n = len(nums)
        while (i < n):
            # when the number is alrd at the correct position
            if (i == nums[i] or nums[i] >= n):
                i += 1
            else:
                # swap the values (nums[nums[i]] is where nums[i] should be)
                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[temp] = temp
        
        # final loop through the sorted array
        for j in range(n):
            if nums[j] != j:
                res = j

        return len(nums) if res == -1 else res