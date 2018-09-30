
def is_valid(s):
    if len(s) % 2 != 0:
        return False
    if s[0] in [']', ')', '}']:
        return False

    openers = {
        '{': '}', 
        '(': ')', 
        '[': ']'
    }
    closers = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    stack = []
    for ch in s:
        if ch in openers.keys():
            stack.append(ch)
        else:
            opening = stack.pop()
            match = closers[ch]
            if opening != match:
                return False

    if len(stack) == 0:
    	return True
    else:
    	return False


if __name__ == '__main__':
    print(is_valid("(])[{]{}([])"))

    print('\n')
    print(is_valid("{}[]()[]{}"))

    print('\n')
    print(is_valid("([)]"))

    print('\n')
    print(is_valid("()"))

    print('\n')
    print(is_valid("(])[{]{}([}{}])"))

    print('\n')
    print(is_valid("{[()]}"))

    print('\n')
    print(is_valid("(]"))

    print('\n')
    print(is_valid("(([]){})"))
