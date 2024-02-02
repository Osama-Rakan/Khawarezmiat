# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if root == None:
            return []

        queue = deque([root])
        answer = []
        while queue:
            queue_length = len(queue)
            level = []
            while queue_length:
                current = queue.popleft()
                level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                
                queue_length -= 1

            answer.append(level)

        return answer