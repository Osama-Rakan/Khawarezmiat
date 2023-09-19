# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def DFS(root, sum1=0):
            if root == None:
                return False

            sum1 += root.val
            isLeaf = root.left == None and root.right == None

            if sum1 == targetSum and isLeaf:
                return True

            return DFS(root.left, sum1) or DFS(root.right, sum1)

        return DFS(root, 0)
