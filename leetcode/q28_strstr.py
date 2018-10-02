
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) > len(haystack):
        return -1
    if len(needle) == len(haystack):
        return 0 if needle == haystack else -1
    
    needle_length = len(needle)
    
    i = 0
    while i <= len(haystack) - len(needle):
        print(haystack[i:i+needle_length])
        if needle == haystack[i:i+needle_length]:
            return i
        i += 1
    return -1



if __name__ == '__main__':
    print(strStr('mississippi', 'pi'))
