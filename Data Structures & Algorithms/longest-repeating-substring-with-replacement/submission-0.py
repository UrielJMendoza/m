class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## Dynamic sliding window

        left = 0
        length = 0 
        counts = {}
        max_freq = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(max_freq, counts[s[right]])

            if (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            length = max(length, right - left + 1)
        return length