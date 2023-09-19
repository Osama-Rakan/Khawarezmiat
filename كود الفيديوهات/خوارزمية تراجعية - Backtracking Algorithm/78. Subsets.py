class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def DFS(index=0, subset=[]):
            if index == len(nums):
                ans.append(subset.copy())
                return
        
            subset.append(nums[index])

            left = DFS(index+1, subset)

            subset.pop()
            right = DFS(index+1, subset)
        
        DFS(0, [])
        return ans
