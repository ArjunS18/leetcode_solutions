#https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(root, level, res):
            if not root:
                return 
            if len(res) < level+1:
                res.append([])
            res[level].append(root.val)
            if (root.left or root.right):
                dfs(root.left, level+1, res)
                dfs(root.right, level+1, res)
            
            return res
        res = []
        res = dfs (root, 0, res)
        return res
      

                
