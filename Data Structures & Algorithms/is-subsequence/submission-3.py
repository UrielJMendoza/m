class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        tracker = 0 
        for i in range(len(t)):
            if s[tracker] == t[i]:
                tracker += 1
                if tracker == len(s):
                    return True
            else:
                continue
        return False


            