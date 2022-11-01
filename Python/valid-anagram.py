class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        CharCountS, CharCountT = {}, {}

        for i in range(len(s)):
            CharCountS[s[i]] = 1 + CharCountS.get(s[i], 0)
            CharCountT[t[i]] = 1 + CharCountT.get(t[i], 0)
        return CharCountS == CharCountT