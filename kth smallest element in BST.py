#https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        def inorderTraversal(root, outlist):
            if root == None:
                return
            if (root):
                
                inorderTraversal(root.left, outlist)
                outlist.append(root.val)
                inorderTraversal(root.right, outlist)
            
            return outlist
        
        outlist = []
        flist = inorderTraversal(root, outlist)
        return flist[k-1]
