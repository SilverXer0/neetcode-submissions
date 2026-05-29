from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            ordlist = [0] * 26
            for char in s:
                ordlist[ord(char) - ord('a')] += 1
            res[tuple(ordlist)].append(s)
        return list(res.values())


