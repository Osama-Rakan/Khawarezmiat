class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            swap_flag = False
            for j in range(0, len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                    swap_flag = True
            if not swap_flag:
                return nums
        return nums