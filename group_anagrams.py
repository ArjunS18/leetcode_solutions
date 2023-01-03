#https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for st in strs:
            cnt_list = [0] * 26
            for c in st:
                cnt_list[ord(c) - ord('a')] += 1
            res[tuple(cnt_list)].append(st)
        return(res.values())
        
