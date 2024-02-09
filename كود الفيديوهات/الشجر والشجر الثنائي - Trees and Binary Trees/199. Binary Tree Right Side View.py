# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if root == None:
            return []

        queue = deque([root])
        answer = []
        while queue:
            queue_length = len(queue)
            while queue_length:
                current = queue.popleft()

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                
                queue_length -= 1

            answer.append(current.val)

        return answer