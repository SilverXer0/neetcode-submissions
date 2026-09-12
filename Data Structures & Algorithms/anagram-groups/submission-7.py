class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for string in strs:
            sorted_string = str(sorted(list(string)))
            if sorted_string in a:
                a[sorted_string].append(string)
            else:
                a[sorted_string] = [string]

        res = []
        for l in a.values():
            res.append(l)

        return res