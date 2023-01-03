#https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = -99999
        minsum = 0
        for i in nums:
            minsum += i
            if (maxsum < minsum):
                maxsum = minsum
                
            if (minsum < 0):
                minsum = 0
            
        return maxsum
        
        
