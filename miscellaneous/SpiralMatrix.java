class SpiralMatrix {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int noOfRows = matrix.length;
        if(noOfRows == 0){
            return new ArrayList<Integer>();
        }
        int noOfCols = matrix[0].length;
        int row_start = 0;
        int col_start = 0;
        int row_end = noOfRows - 1;
        int col_end = noOfCols - 1;
        while(row_start <= row_end && col_start <= col_end){
            System.out.println(row_start + " " + row_end + " " + col_start + " " + col_end);
            for(int i=col_start;i<=col_end; i++){
                result.add(matrix[row_start][i]);
            }
            for(int i=row_start + 1;i<row_end;i++){
                result.add(matrix[i][col_end]);
            }
            if(row_start != row_end){
                for(int i=col_end;i>=col_start;i--){
                    result.add(matrix[row_end][i]);
                }
            }
            if(col_start != col_end){
                for(int i=row_end-1;i>row_start;i--){
                    result.add(matrix[i][col_start]);
                }
            }
            row_start++;
            col_start++;
            row_end--;
            col_end--;
        }
        return result;
    }
}