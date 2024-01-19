class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, num in enumerate(nums):
            d = target - num

            if d in hash_map:
                return [hash_map[d], index]
            hash_map[num] = index