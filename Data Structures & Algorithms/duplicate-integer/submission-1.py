#Sliding window 2 pointer approach
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        