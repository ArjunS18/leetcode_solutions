#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
 

        
        index = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                index = i
                break
      
        start = 0
        end = len(nums) - 1
        m1 = index - 1
        m2 = index + 1
   
        if nums[index] == target:
            return index
        for i in range(int(len(nums)/2) + 1):
            mid1 = int((start + m1) / 2)
            if start <= m1:
                if nums[mid1] == target:
                    return mid1
                elif nums[mid1] > target:
                    m1 = mid1 - 1
                else:
                    start = mid1 + 1

            mid2 = int((m2 + end) / 2)
            if mid2 <= end:
                if nums[mid2] == target:
                    return mid2
                elif nums[mid2] < target:
                    m2 = mid2 + 1
                else:
                    end = mid2 - 1
        return -1
