class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for string in strs:
            ordlist = [0] * 26
            for char in string:
                ordlist[ord(char) - ord('a')] += 1
            ordtuple = tuple(ordlist)
            if ordtuple in d:
                d[ordtuple].append(string)
            else:
                d[ordtuple] = [string]

        for string_list in d.values():
            res.append(string_list)

        return res


