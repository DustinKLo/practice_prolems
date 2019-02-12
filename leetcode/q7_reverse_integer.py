def reverse(x):
    print("x: {}".format(x))
    digit = 10
    ans = 0

    neg_sign = 1
    if x < 0:
    	x = x * -1
    	neg_sign = -1

    if x > 2147483647:
        return 0

    while(True):
    	y = (x%digit - x%(digit/10)) / (digit/10)
    	ans = ans * 10 + y
    	# print("y: {} \t ans: {}".format(y, ans))
    	
    	if(x / digit == 0):
    		break
    	
    	digit = digit * 10

    if ans > 2147483647:
        return 0 

    return ans * neg_sign


if __name__ == '__main__':
    print(reverse(-123450))
    print('')
    print(reverse(123))
    print('')
    print(reverse(10000001))
    print('')
    print(reverse(13))
    print('')
    print(reverse(10))
    print('')
    print(reverse(7))
    print('')
    print(reverse(1534236469))
