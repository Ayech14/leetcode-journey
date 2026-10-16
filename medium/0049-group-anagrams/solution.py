"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".

The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.

The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

Constraints:

1 <= strs.length <= 10^4

0 <= strs[i].length <= 100

strs[i] consists of lowercase English letters.

"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            # Anagrams have identical letter counts, so the counts are the key.
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
