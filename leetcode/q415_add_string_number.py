class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        remainder = 0
        ans = ""
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 and j >= 0:
            temp = (ord(num1[i]) - 48) + (ord(num2[j]) - 48) + remainder
            if temp > 9:
                temp = temp - 10
                remainder = 1
            else:
                remainder = 0
            ans = str(temp) + ans
            i -= 1
            j -= 1
        
        k = i if i > j else j
        leftover = num1 if i > j else num2
        
        while k >= 0:
            temp = ord(leftover[k]) - 48 + remainder
            if temp > 9:
                temp = temp - 10
                remainder = 1
            else:
                remainder = 0
            ans = str(temp) + ans
            k -= 1
        if remainder > 0:
            return "1" + ans
        else:
            return ans
