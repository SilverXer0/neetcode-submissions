class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_list = [0] * 26
        s2_list = [0] * 26

        for i in range(len(s1)):
            s1_list[ord(s1[i]) - ord('a')] += 1

        matches = 0 
        for i in range(26):
            if s1_list[i] == s2_list[i]:
                matches += 1
        
        left = 0
        for right in range(len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[right]) - ord('a')
            s2_list[idx] += 1
            if s2_list[idx] == s1_list[idx] + 1:
                matches -= 1
            elif s2_list[idx] == s1_list[idx]:
                matches += 1

            if right - left + 1 > len(s1):
                idx_l = ord(s2[left]) - ord('a')
                s2_list[idx_l] -= 1
                if s2_list[idx_l] + 1 == s1_list[idx_l]:
                    matches -= 1
                elif s2_list[idx_l] == s1_list[idx_l]:
                    matches += 1
                left += 1

            
        return matches == 26

            
            

            
