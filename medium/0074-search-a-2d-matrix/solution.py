"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.

The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length

n == matrix[i].length

1 <= m, n <= 100

-10^4 <= matrix[i][j], target <= 10^4
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            # Map the flat index back to a row and column.
            value = matrix[mid // cols][mid % cols]

            if value == target:
                return True

            if value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
