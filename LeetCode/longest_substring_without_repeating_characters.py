#see https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        chars = set()
        ans, l, r = 0, 0, 0
        while (l < n and r < n):
            if (not s[r] in chars):
                chars.add(s[r])
                r += 1
                ans = max(ans, r - l)
            else:
                chars.remove(s[l])
                l += 1
        return ans
