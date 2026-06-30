class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_track = {}
        s_track = {}
        res = ""
        reslen = float('inf')

        for i in range(len(t)):
            t_track[t[i]] = 1 + t_track.get(t[i], 0)

        l = 0
        need = len(t_track)
        have = 0

        for r in range(len(s)):
            s_track[s[r]] = 1 + s_track.get(s[r], 0)
            if s[r] in t_track and s_track[s[r]] == t_track[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    res = s[l:r + 1]
                s_track[s[l]] -= 1
                if s[l] in t_track and s_track[s[l]] < t_track[s[l]]:
                    have -= 1
                l += 1
        
        return res
        
