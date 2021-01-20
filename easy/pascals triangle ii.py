class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
                
        if rowIndex == 0:
            return [1]
        
        triangle.append([1])
        
        for i in range(1, rowIndex+1):
            prevRow = triangle[i-1]
            newRow = []
            
            newRow.append(1)
            for j in range(1, len(prevRow)):
                newRow.append(prevRow[j-1] + prevRow[j])
            
            newRow.append(1)
            triangle.append(newRow)
        
        return triangle[-1]