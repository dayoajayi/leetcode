class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        int rows = 0;
        int cols = matrix[0].length - 1;
        
        while (rows < matrix.length && cols >= 0)
        {
            if (matrix[rows][cols] == target)
            {
                return true;
            }
            else if (matrix[rows][cols] > target)
            {
                // shrink matrix by one col to the left
                cols -= 1;                
            }
            else
            {                
                rows += 1;
            }            
        }        
        return false;
    }
}


/*
matrix = [
           [1,4,7,11,15],
           [2,5,8,12,19],
           [3,6,9,16,22],
           [10,13,14,17,24],
           [18,21,23,26,30]
         ]
*/