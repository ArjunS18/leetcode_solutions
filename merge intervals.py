#https://leetcode.com/problems/merge-intervals/
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x:x[0])
        #print(intervals)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            lastele = result[-1][1]
            #print(lastele)
            if intervals[i][0] <= lastele :
                maxi = max(intervals[i][1], lastele)
                result[-1][1] = maxi
            else:
                result.append(intervals[i])

        return(result)
            
        
