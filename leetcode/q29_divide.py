
def divide(dividend, divisor):
    if divisor == 0:
        return float('inf')
    if dividend == 0:
        return 0

    sign = -1 if dividend < 0 or divisor < 0 else 1
    divisor, dividend = abs(divisor), abs(dividend)
    
    ans = 0
    start = 0
    while True:
        start += divisor
        if start > dividend:
            break
        ans += 1

    return ans * sign


if __name__ == '__main__':
    print(divide(10, -3))
    print(divide(1, 1))
    print(divide(-1, 1))
    print(divide(1, -1))
    print(divide(0, 1))
    print(divide(-1, -1))
    # print(divide(-2147483648, -1))
