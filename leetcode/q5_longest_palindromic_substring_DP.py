class Solution:
    @staticmethod
    def print_hash_tbl(tbl, s):
        str_to_list = [ch for ch in s]
        print('   ' + ', '.join(str_to_list))
        for j in range(len(tbl)):
            print(s[j], tbl[j])

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_len = len(s)
        hash_tbl = [[0] * str_len for i in range(str_len)]

        if str_len == 0:
            return ""
        if str_len == 1:
            return s[0]

        longest_length = 0
        longest_str = ""

        l = 0  # left bound
        r = 0  # right bound, will increment by 1 after we check palindromes by length of 1, 2, 3, etc until we reach the end

        # as long as difference between left and right boundaries and less than string length
        while r - l < str_len:
            i = l
            j = r

            while j < str_len:
                is_palindrome = False

                if j - i == 0:  # string length 1
                    hash_tbl[i][j] = 1
                    is_palindrome = True

                elif j - i == 1 and s[i] == s[j]:  # string length 2, check if letters are equal
                    hash_tbl[i][j] = 1
                    is_palindrome = True

                # string length 3, check if i + 1, j - 1 is palindrome, then check if s[i] == s[j]
                elif hash_tbl[i + 1][j - 1] == 1 and s[i] == s[j]:
                    hash_tbl[i][j] = 1
                    is_palindrome = True

                if is_palindrome is True:
                    if j - i + 1 > longest_length:
                        longest_length = j - i + 1
                        longest_str = s[i:j + 1]

                i += 1
                j += 1
            r += 1

        self.print_hash_tbl(hash_tbl, s)
        print("longest palindrome '%s' with length %d" % (longest_str, longest_length))
        print("##############################\n")
        return longest_str



if __name__ == '__main__':
    s = Solution()
    s.longestPalindrome("aa")
    s.longestPalindrome("ba")
    s.longestPalindrome("abcbac")
    s.longestPalindrome("forgeeksskeegfor")
    s.longestPalindrome("forforforgeeksskeegzzz")
    s.longestPalindrome("gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhasdsa")
