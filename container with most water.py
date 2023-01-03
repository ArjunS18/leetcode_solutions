#https://leetcode.com/problems/container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        fpt = 0
        lpt = len(height) - 1
        max_water = 0
        for i in range(len(height)):
            mini = min(height[fpt], height[lpt])
            curr = mini * (abs(fpt-lpt))
            if height[fpt] < height[lpt]:
                fpt += 1
            else:
                lpt -= 1

            max_water = max(max_water, curr)
        return (max_water)

        
