#https://leetcode.com/problems/set-matrix-zeroes/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
     
        rlist = []
        clist = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rlist.append(r)
                    clist.append(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rlist or c in clist:
                    matrix[r][c] = 0
