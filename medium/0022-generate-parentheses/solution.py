"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8

"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        # The stack holds the parentheses chosen so far.
        stack = []

        def build(opened: int, closed: int) -> None:
            if closed == n:
                result.append("".join(stack))
                return

            # We may open another pair while we have some left.
            if opened < n:
                stack.append("(")
                build(opened + 1, closed)
                stack.pop()

            # We may close only if there is an unmatched "(".
            if closed < opened:
                stack.append(")")
                build(opened, closed + 1)
                stack.pop()

        build(0, 0)
        return result
