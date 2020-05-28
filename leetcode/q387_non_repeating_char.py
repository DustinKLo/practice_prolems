
def first_consecutive_non_repeat_char(s):
    if len(s) == 0:
        return -1
    if len(s) == 1:
        return 0
    
    is_repeat = False
    
    for i in range(0, len(s) - 1):
        tracking_char = s[i]
        next_char = s[i+1]
        print(i, tracking_char, next_char)
        
        if tracking_char == next_char:
            next_char = tracking_char
            is_repeat = True
            continue

        if is_repeat is False:
            return i
        is_repeat = False # fail safe if tracking_char is repeated
    
    # if reached the end and hahve not encountered a repeated character
    if tracking_char != next_char:
        return i + 1
    return -1


if __name__ == '__main__':
    print(first_consecutive_non_repeat_char("aaabbbcdddeeefff"))
    print("")
    print(first_consecutive_non_repeat_char("abbbcdddeeefff"))
    print("")
    print(first_consecutive_non_repeat_char("aaabbbccdddeeef"))
    print("")
    print(first_consecutive_non_repeat_char("aaabbbccdddeeeff"))
    print("")
    print(first_consecutive_non_repeat_char("aa"))
    print("")
    print(first_consecutive_non_repeat_char("a"))
    print("")
    print(first_consecutive_non_repeat_char(""))
    print("")
    print(first_consecutive_non_repeat_char("aabcdefghijklmnopqrstuvwxyz"))
