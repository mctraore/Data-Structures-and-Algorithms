class Solution:
    def rob(self, nums):
        
        if nums == None:
            return 0
        elif len(nums)==1:
            return nums[0]
        
        prev = 0
        current = 0
        
        for house in nums:
            temp = prev
            prev = current
            
            current = max(temp+house, current)
            
        return current