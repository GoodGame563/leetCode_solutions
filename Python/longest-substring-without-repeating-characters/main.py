class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenght = len(s)
        if lenght == 0 or lenght == 1:
            return lenght
        result = min(1, lenght)
        left = 0
        see = {}
        see [s[0]] = 0
        for i in range(1, lenght):
            left = max(left, see.get(s[i], -1) + 1)
            see[s[i]] = i
            result = max(result, i - left + 1)
        return result 



print(Solution().lengthOfLongestSubstring("tmmzuxt"))
