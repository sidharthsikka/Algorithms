class BattleshipsBoard {
    public int countBattleships(char[][] board) {
        int count = 0;
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[0].length;j++){
                if(board[i][j] == 'X' && (i-1<0 || (i-1>-1 && board[i-1][j] != 'X')) && (j-1<0 || (j-1>-1 && board[i][j-1] != 'X'))){
                    count++;
                }
            }
        }
        return count;
    }
}