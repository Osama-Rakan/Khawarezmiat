class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 # slow
        r = 1 # fast
        while r < len(nums):
            if nums[l] == 0 and nums[r] !=0:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp

            r += 1
            if nums[l] != 0:
                l += 1