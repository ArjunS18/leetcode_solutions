#https://leetcode.com/problems/find-the-duplicate-number/description/
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dupset = {}
        dupset = set()
        for i in range(0, len(nums)):
            if nums[i] not in dupset:
                dupset.add(nums[i])
            else:
                return nums[i]
    
