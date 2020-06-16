class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapper = {
            ']': '[',
            ')': '(',
            '}': '{',
        }
        stack = []

        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.insert(0, c)
            else:
                if len(stack) == 0:
                    return False
                if c == ")" and stack[0] == "(":
                    stack.pop(0)
                elif c == "]" and stack[0] == "[":
                    stack.pop(0)
                elif c == "}" and stack[0] == "{":
                    stack.pop(0)
                else:
                    return False
        return True if len(stack) == 0 else False


if __name__ == '__main__':
    s = Solution()
    t = "()"
    print(t, s.isValid(t))
    t = "()[]{}"
    print(t, s.isValid(t))
    t = "(]"
    print(t, s.isValid(t))
    t = "([)]"
    print(t, s.isValid(t))
    t = "{[]}"
    print(t, s.isValid(t))
    t = "}"
    print(t, s.isValid(t))
    t = "(])[{]{}([])"
    print(t, s.isValid(t))
    t = "{}[]()[]{}"
    print(t, s.isValid(t))
    t = "([)]"
    print(t, s.isValid(t))
    t = "()"
    print(t, s.isValid(t))
    t = "(])[{]{}([}{}])"
    print(t, s.isValid(t))
    t = "{[()]}"
    print(t, s.isValid(t))
    t = "(]"
    print(t, s.isValid(t))
    t = "(([]){})"
    print(t, s.isValid(t))
