class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_track = {}
        t_track ={}

        for i in range(len(t)):
            t_track[t[i]] = 1 + t_track.get(t[i], 0)

        left = 0
        have = 0
        need = len(t_track)
        reslen = float('inf')
        res = ""

        for right in range(len(s)):
            s_track[s[right]] = 1 + s_track.get(s[right], 0)
            if s[right] in t_track and s_track[s[right]] == t_track[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < reslen:
                    reslen = right - left + 1
                    res = s[left:right + 1]
                s_track[s[left]] -= 1
                if s[left] in t_track and s_track[s[left]] < t_track[s[left]]:
                    have -= 1
                left += 1

        return res
