# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs with a maxLen counter
        def maxLen(node: TreeNode):
            if node is None:
                return 0
            return max(1 + maxLen(node.left), 1 + maxLen(node.right))
        

        return maxLen(root)
