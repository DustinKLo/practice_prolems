import math

class Solution(object):
    def getPermutationSlow(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        num_set = ''.join(str(c) for c in range(1, n + 1))
        print(num_set, k)

        self.count = 0
        self.target = k
        self.ans = ""
        def traverse(s, chars, i, n):
            if i == n:  # base case
                self.count += 1
                if self.count == self.target:
                    self.ans = s
                return
            if self.count < self.target:
                for idx in range(len(chars)):
                    traverse(s + chars[idx], chars[:idx] + chars[idx+1:], i + 1, n)
        traverse("", num_set, 0, n)
        print(self.ans)
        print("############################################")
        return self.ans

    def getPermutation(self, n, k):
        if k < 1 or k > math.factorial(n):
            return ""

        num_set = ''.join(str(c) for c in range(1, n + 1))
        letters_remaining = len(num_set)

        print(num_set, k)
        k -= 1
        
        ans = ""
        start = 0
        
        while letters_remaining > 0:
            num_options = math.factorial(letters_remaining)
            choice_per_option = int(num_options / letters_remaining)
            idx = int(k / choice_per_option)
            left_bound = choice_per_option * idx
            k = k - left_bound
            
            ans += num_set[idx]
            num_set = num_set[:idx] + num_set[idx + 1:]
            
            start += 1
            letters_remaining -= 1

        print(ans)
        print("############################################")
        return ans



if __name__ == '__main__':
    s = Solution()
    s.getPermutationSlow(3, 3)
    s.getPermutation(3, 3)
    s.getPermutationSlow(4, 9)
    s.getPermutation(4, 9)
    s.getPermutationSlow(4, 17)
    s.getPermutation(4, 17)
    s.getPermutationSlow(7, 100)
    s.getPermutation(7, 100)
    s.getPermutationSlow(9, 100000)
    s.getPermutation(9, 100000)
