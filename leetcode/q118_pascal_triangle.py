class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        
        n = 2
        rows = [[1], [1,1]]
        while n < numRows:
            curRow = rows[-1]
            # print(n, curRow, len(curRow))
            newRow = [1]
            for i in range(1, len(curRow)):
                newRow.append(curRow[i-1] + curRow[i])
            newRow.append(1)
            rows.append(newRow)
            n += 1    
        return rows
