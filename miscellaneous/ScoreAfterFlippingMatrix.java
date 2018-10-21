class ScoreAfterFlippingMatrix {
    public int matrixScore(int[][] A) {
        int rows = A.length;
        int cols = A[0].length;
        int res = (1 << (cols-1)) * rows;
        for(int i=1;i<cols;i++){
            int curr = 0;
            for(int j=0;j<rows;j++){
                curr += A[j][i] == A[j][0] ? 1:0;
            }
            res += (Math.max(curr, rows-curr) * (1 << (cols - 1 - i)));
        }
        return res;
    }
}