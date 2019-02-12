def check_palindrome(x):
    print("x: {}".format(x))
    digit = 10
    ans = 0

    neg_sign = 1
    if x < 0:
        return False

    if x == 0:
        return True

    if x % 10 == 0:
        return False

    while(True):
    	y = (x%digit - x%(digit/10)) / (digit/10)
    	ans = ans * 10 + y
    	# print("y: {} \t ans: {}".format(y, ans))
    	
    	if(x / digit == 0):
    		break
    	
    	digit = digit * 10

    if ans == x:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_palindrome(-123450))
    print('')
    print(check_palindrome(0))
    print('')
    print(check_palindrome(1234567890987654321))
