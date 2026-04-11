from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, max_freq, result = 0, 0, 0
        count = defaultdict(int)
        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])
            while (right - left + 1) - max_freq >k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result

print(Solution().characterReplacement("AABABBA", 1))
