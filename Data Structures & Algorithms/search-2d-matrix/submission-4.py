class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])

        left, right = 0, numRows * numCols - 1

        while(left <= right):
            index = (left + right) // 2
            # compute the array index with this index now.
            rowIndex, colIndex = index // numCols, index%numCols

            print(rowIndex, colIndex)
            if(matrix[rowIndex][colIndex] > target):
                right-=1
            elif(matrix[rowIndex][colIndex] < target):
                left+=1
            else:
                return True
        

        return False