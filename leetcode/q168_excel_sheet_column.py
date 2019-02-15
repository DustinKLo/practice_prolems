class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        mapper = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        loop_counter = 1
        
        ans = ""
        while n / 26 != 0:
            index = 26 if n % 26 == 0 else n % 26
            if n % 26 == 0:
                n = n - 1
            print(n, n / 26, n % 26, index, mapper[index], loop_counter)
            ans = mapper[index] + ans
            n = n / 26
            loop_counter += 1
            
        print("out of loop")
        print(n, n / 26, n % 26, mapper[n % 26], loop_counter) 
        ans = mapper[n % 26] + ans

        return ans
