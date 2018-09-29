
def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    print(dividend, divisor)
    sign = False
    if dividend < 0:
        sign = not sign
        dividend = -dividend
    if divisor < 0:
        sign = not sign
        divisor = -divisor
    
    result = 0
    while dividend >= divisor:
        mult_divisor = divisor
        mult_result = 1
        while (mult_divisor + mult_divisor) <= dividend:
            mult_divisor = mult_divisor + mult_divisor
            print('mult_divisor: {}'.format(mult_divisor))
            mult_result = mult_result + mult_result
            print('mult_result: {}'.format(mult_result))
        print(mult_divisor)
        result += mult_result
        print('result: {}'.format(result))
        print('mult_divisor: {}'.format(mult_divisor))
        dividend -= mult_divisor
        print('dividend: {}'.format(dividend))

    if sign:
        result = -result
    
    if result > 2147483647:
        result = 2147483647
    
    return 'answer is:{}'.format(result)


if __name__ == '__main__':
    # print(divide(10, -3))
    # print('\n')
    # print(divide(1, 1))
    # print('\n')
    # print(divide(-1, 1))
    # print('\n')
    # print(divide(1, -1))
    # print('\n')
    # print(divide(0, 1))
    # print('\n')
    # print(divide(-1, -1))
    # print('\n')
    # print(divide(-2147483648, -1))
    # print('\n')
    # print(divide(-2147483648, -2))
    # print('\n')
    # print(divide(-2147483648, -3))
    # print('\n')
    print(divide(100000, 3))
