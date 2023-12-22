class Solution:
    def maxScore(self, s: str) -> int:
        max_score = -1
        left_zeros = 0
        right_ones = 0

        for character in s: # O(n)
            if character == '1':
                right_ones += 1
        
        for index, character in enumerate(s): # O(n)
            if index == len(s)-1:
                return max_score

            if character == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            
            if left_zeros+right_ones > max_score:
                max_score = left_zeros+right_ones