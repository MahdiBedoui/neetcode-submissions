class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 1
        output = 0 
        current = 0
        for i in range(len(nums)):
            if nums[i] == x:
                current += 1
            else:
                current = 0
            if current > output:
                output = current
        return output
