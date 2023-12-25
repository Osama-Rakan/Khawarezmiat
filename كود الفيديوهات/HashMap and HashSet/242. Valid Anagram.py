class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for character in s: # O(m)
            if character not in hash_map: # O(1)
                hash_map[character] = 1
                continue
            hash_map[character] += 1

        zero_counter = 0
        for character in t: # O(n)
            if character not in hash_map: # O(1)
                return False
            hash_map[character] -= 1
            if hash_map[character] == 0:
                zero_counter += 1
        
        return zero_counter == len(hash_map)