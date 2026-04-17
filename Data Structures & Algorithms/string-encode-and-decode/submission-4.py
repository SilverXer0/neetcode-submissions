class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = []
            while s[i] != '#':
                length.append(s[i])
                i += 1
            i += 1
            length = int("".join(length))
            temp = []
            for j in range(length):
                temp.append(s[i])
                i += 1
            res.append("".join(temp))
        return res
