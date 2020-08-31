class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = set()

        def traverse(a, leftovers, counter):
            """
            s: list[str], answer we are building to
            leftovers: str, letters leftovers
            """
            if counter == 4:  # end case
                if len(leftovers) == 0 and len(a) == 4:
                    ans = '.'.join(a)
                    self.ans.add(ans)
                return

            if len(leftovers) == 0:
                return

            traverse(a + [leftovers[:1]], leftovers[1:], counter + 1) # 1st letter

            if leftovers[0] != '0':  # check if first letter is 0, if != 0
                traverse(a + [leftovers[:2]], leftovers[2:], counter + 1)  # 2nd letter

                if int(leftovers[:3]) <= 255:  # 3rd letter
                    traverse(a + [leftovers[:3]], leftovers[3:], counter + 1)

        traverse([], s, 0)
        print(s)
        for ans in self.ans:
        	print(ans)
        print("####################################\n")
        return self.ans


if __name__ == '__main__':
    s = Solution()

    s.restoreIpAddresses('25525511135')
    s.restoreIpAddresses('0000')
    s.restoreIpAddresses('1111')
    s.restoreIpAddresses('010010')
    s.restoreIpAddresses('101023')
