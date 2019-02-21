def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if len(digits) == 1:
        if digits[0] == 9:
            return [1,0]
        else:
            digits[0] = digits[0] + 1
            return digits
    
    if digits[-1] == 9:
        digits[-1] = 0
        remainder = 1
    else: 
        digits[-1] += 1
        remainder = 0
    
    print(digits)
    for i in range(len(digits) - 2, -1, -1):
        if remainder == 1:
            if digits[i] == 9:
                digits[i] = 0
                remainder = 1
            else:
                digits[i] += 1
                remainder = 0
        else:
            remainder = 0
            
    
    print(remainder)
    print(digits)
    if remainder == 1:
        if digits[0] > 1 and digits[0] < 9:
            digits[0] += 1
        elif digits[0] == 0:
            digits.insert(0, 1)
    
    return digits

if __name__ == "__main__":
    pass
