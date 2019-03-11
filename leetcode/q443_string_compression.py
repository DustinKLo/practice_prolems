class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        cur_letter = chars[0]
        ans = []
        cur_letter_count = 0
        while i < len(chars):
            # print(chars[i])
            if chars[i] == cur_letter:
                cur_letter_count += 1
            else:
                ans.append(cur_letter)
                ans.append(cur_letter_count)
                cur_letter = chars[i]
                cur_letter_count = 1
            i += 1
        ans.append(cur_letter)
        ans.append(cur_letter_count)
        # print(ans)
        if len(ans) < len(chars):
            return len(ans)
