#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lp = 0
        rp = len(numbers) - 1
        em = []
        for i in range(0, len(numbers) - 1):
            if (numbers[lp] + numbers[rp] == target):
                return lp + 1, rp + 1
            elif (numbers[lp] + numbers[rp] < target):
                lp = lp + 1
            elif (numbers[lp] + numbers[rp] > target):
                rp = rp - 1
        return em
