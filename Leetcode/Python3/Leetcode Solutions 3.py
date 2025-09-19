class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # stores the last seen index of each character
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in char_index and char_index[ch] >= left:   
                left = char_index[ch] + 1
            char_index[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len