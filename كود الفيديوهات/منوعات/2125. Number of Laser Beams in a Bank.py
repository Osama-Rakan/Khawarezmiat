class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        p = 0
        c = 0
        ans = 0

        for row in bank:
            for character in row:
                if character == '1':
                    c += 1
            
            if c > 0:
                ans += p * c
                p = c
                c = 0
        
        return ans