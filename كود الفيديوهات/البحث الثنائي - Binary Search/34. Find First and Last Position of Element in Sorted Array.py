class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        left_i = -1
        while l <= r:
            m = (r+l)//2

            if nums[m] == target:
                left_i = m
                r = m-1

            if nums[m] < target:
                l = m+1
            if nums[m] > target:
                r = m-1

        l, r = 0, len(nums)-1
        right_i = -1
        while l <= r:
            m = (r+l)//2

            if nums[m] == target:
                right_i = m
                l = m+1

            if nums[m] < target:
                l = m+1
            if nums[m] > target:
                r = m-1
        return [left_i, right_i]