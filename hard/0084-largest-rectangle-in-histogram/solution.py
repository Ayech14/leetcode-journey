"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

Input: heights = [2,4]
Output: 4

Constraints:

1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0

        # Stack of (start index, height), heights strictly increasing.
        stack = []

        for i, h in enumerate(heights):
            start = i

            # Taller bars on the stack end here, so finish their rectangles.
            while stack and stack[-1][1] >= h:
                index, height = stack.pop()
                best = max(best, height * (i - index))
                # The current bar can extend back to where that bar started.
                start = index

            stack.append((start, h))

        # Bars left on the stack extend to the end of the histogram.
        for index, height in stack:
            best = max(best, height * (len(heights) - index))

        return best
