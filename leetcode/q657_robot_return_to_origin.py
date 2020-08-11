class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        origin = [0, 0]
        for m in moves:
            if m == "U":
                origin[1] += 1
            elif m == "D":
                origin[1] -= 1
            elif m == "L":
                origin[0] -= 1
            else: # right
                origin[0] += 1
        
        return origin == [0, 0]
