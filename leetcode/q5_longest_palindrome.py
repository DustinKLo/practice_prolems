
def check_palindrome(s):
    if s == s[::-1]:
        return True
    return False

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    if len(s) <= 1:
        return s

    palindrome = s[0]
    for i in range(0, len(s)-1):
        for j in range(i+2, len(s)+1):
            word = s[i:j]
            if check_palindrome(word):
                # print(word)
                if len(word) > len(palindrome):
                    palindrome = word

    return palindrome


if __name__ == '__main__':
    x = longestPalindrome("gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhasdsa")
    print(x)
    print(len(x))