# Newton's method
# x_n = x_n-1 - (f(x) - x) / f'(x)
class Solution:
    def isPerfectSquare(self, num):
        x_n_minus_1 = (float(num) + 1)/2
        i = 0
        while i < 20:
            x_n = x_n_minus_1 - (x_n_minus_1 ** 2 - num) / float(2 * x_n_minus_1)
            i += 1
            
            if abs(x_n - x_n_minus_1) == 0.0:
                break
            x_n_minus_1 = x_n
            # print(x_n)
         
        return x_n == int(x_n)
