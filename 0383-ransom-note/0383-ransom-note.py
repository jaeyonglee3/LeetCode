class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # in other words, do ransomNote and magazine strings contain
        # the same count of each letter?
        if len(ransomNote) > len(magazine):
            return False

        count_r = {}
        count_m = {}

        for c in ransomNote:
            count_r[c] = count_r.get(c, 0) + 1
        
        for c in magazine:
            if c not in count_r or count_r.get(c, -1) == count_m.get(c, -2):
                continue

            count_m[c] = count_m.get(c, 0) + 1
        
        return count_r == count_m