class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def DFS(index=0, subset=[]):
            if index == len(nums):
                ans.append(subset.copy())
                return
        
            subset.append(nums[index])

            left = DFS(index+1, subset)
            subset.pop()

            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1

            right = DFS(index+1, subset)
        
        DFS(0, [])
        return ans
