class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1, m2 = {}, {}
        for char in s:
            if char not in m1:
                m1[char] = 1
            else:
                m1[char] += 1
        for char in t:
            if char not in m2:
                m2[char] = 1
            else:
                m2[char] += 1
        
        return m1 == m2