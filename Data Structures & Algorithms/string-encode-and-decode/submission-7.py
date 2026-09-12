class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s) - 1:
            l = ""
            while s[i] != '#':
                l += s[i]
                i += 1
            l = int(l)
            i += 1
            j = i + l
            t = "" 
            while i < j:
                t += s[i]
                i += 1
            res.append(t)
        return res
            

