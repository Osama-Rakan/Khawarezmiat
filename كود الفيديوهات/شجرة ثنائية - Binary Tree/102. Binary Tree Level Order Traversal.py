# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        queue = [root]
        ans = []

        while queue:
            queue_length = len(queue)
            level = []

            while queue_length > 0:
                current = queue.pop(0)
                level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                queue_length -= 1
            ans.append(level)
        
        return ans
