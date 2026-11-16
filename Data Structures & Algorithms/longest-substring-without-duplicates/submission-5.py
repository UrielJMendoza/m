class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      



        res = 0
        seen = set()
        left = 0
        ##use seen set have two pointer left right



        for right in range(len(s)):
            ##go through len s with right

            while s[right] in seen:
                seen.remove(s[left])
                left +=1


            seen.add(s[right])
            res = max(res, right - left + 1)



        return res

        