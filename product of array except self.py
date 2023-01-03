#https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = [0] * len(nums)
        suf = [0] * len(nums)
        res = [0] * len(nums)
        pre[0] = 1
        suf[len(nums) - 1] = 1
        for i in range (1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        for j in range((len(nums) - 2), -1, -1):
            suf[j] = suf[j+1] * nums[j+1]
            
        for i in range(0, len(nums)):
            res[i] = pre[i] * suf[i]
            
        return res
