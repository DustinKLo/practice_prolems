class Solution(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if rowIndex < 1:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 2:
            return [1,2,1]
        
        n = 2
        rows = [1,1]
        while n <= rowIndex:
            curRow = rows
            # print(n, curRow, len(curRow))
            newRow = [1]
            for i in range(1, len(curRow)):
                newRow.append(curRow[i-1] + curRow[i])
            newRow.append(1)
            rows = newRow
            n += 1    
        return rows
