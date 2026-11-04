"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

m == s.length

n == t.length

1 <= m, n <= 10^5

s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        # How many characters (with duplicates) the window still has to cover.
        missing = len(t)

        best_start = 0
        best_len = len(s) + 1
        left = 0

        for right, char in enumerate(s):
            # Only characters we still need reduce the missing count.
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            # The window is valid: shrink it from the left as far as possible.
            while missing == 0:
                if right - left + 1 < best_len:
                    best_start = left
                    best_len = right - left + 1

                need[s[left]] += 1
                # Dropping a needed character makes the window invalid again.
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        if best_len > len(s):
            return ""
        return s[best_start:best_start + best_len]
