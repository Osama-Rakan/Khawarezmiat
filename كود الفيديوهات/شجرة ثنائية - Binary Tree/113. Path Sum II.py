# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def DFS(root, sum1=0, path=[]):
            if root == None:
                return None
            
            sum1 += root.val
            path.append(root.val)

            isLeaf = root.right == None and root.left == None

            if isLeaf and sum1 == targetSum:
                paths.append(path.copy())


            DFS(root.left, sum1, path)
            DFS(root.right, sum1, path)

            path.pop()
        
        DFS(root, 0, [])
        return paths
