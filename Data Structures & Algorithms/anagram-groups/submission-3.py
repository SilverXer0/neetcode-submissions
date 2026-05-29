class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for string in strs:
            sorted_str = "".join(sorted(list(string)))
            if sorted_str in d:
                d[sorted_str].append(string)
            else:
                d[sorted_str] = [string]

        for string_list in d.values():
            res.append(string_list)

        return res


