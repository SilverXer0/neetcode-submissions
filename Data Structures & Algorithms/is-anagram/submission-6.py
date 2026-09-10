class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l =[0] * 26
        for i in range(len(s)):
            l[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            l[ord(t[i]) - ord('a')] -= 1

        for n in l:
            if n != 0:
                return False

        return True