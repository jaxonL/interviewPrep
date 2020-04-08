# April 6, 2020 - Daily Interview Pro
# Hi, here's your problem today. This problem was recently asked by Uber:
# Imagine you are building a compiler. Before running any code, the compiler
# must check that the parentheses in the program are balanced. Every opening
# bracket must have a corresponding closing bracket. We can approximate this using strings.

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.

# Example:
# Input: "((()))"
# Output: True
# Input: "[()]{}"
# Output: True
# Input: "({[)]"
# Output: False

class Solution:
    def __init__(self):
        self.openers = '{(['
        self.closers = '})]'
        self.opener_matchers = {
            '}' : '{',
            ')' : '(',
            ']': '['
        }

    def isValid(self, s):
        parens_stack = []
        for chara in s:
            if chara in self.openers:
                parens_stack.append(chara)
            elif chara in self.closers:
                if len(parens_stack) == 0:
                    return False
                # len(parens_stack) > 0
                # previous parens opener must have been equal to currently closing char
                prev_opener = parens_stack.pop()
                expected_opener = self.opener_matchers[chara]
                if prev_opener != expected_opener:
                    return False
                # else continue
            # else continue
            # can be for cases where we have other characters in the strings
        # should have nothing in the stack
        return len(parens_stack) == 0


if __name__ == '__main__':
    # Test Program
    s = "()(){(())" 
    # should return False
    print(Solution().isValid(s))

    s = ''
    # should return True
    print(Solution().isValid(s))

    s = "([{}])()"
    # should return True
    print(Solution().isValid(s))
