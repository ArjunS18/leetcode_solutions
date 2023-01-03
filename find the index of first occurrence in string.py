#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (not needle):
            return 0
      
        hlen = len(haystack)
        for i in range (0, hlen):
        
            if(haystack[i:i+len(needle)] == needle):
                return i
            

            
        return -1
