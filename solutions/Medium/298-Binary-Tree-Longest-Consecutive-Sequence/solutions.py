# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxi = 1
        def dfs(tree,currMax,prevVal=None):
            self.maxi = max(currMax,self.maxi)
            if tree:
                prev = tree.val
                if prevVal!=None and prev - prevVal == 1:
                    dfs(tree.left,currMax+1,prev)
                    dfs(tree.right,currMax+1,prev)
                else:
                    dfs(tree.left,1,prev)
                    dfs(tree.right,1,prev)
                    
        dfs(root,1)
        return self.maxi