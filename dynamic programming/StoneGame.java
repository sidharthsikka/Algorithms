class Solution {    
    public boolean stoneGame(int[] piles) {
            return gameDP(piles);
    }
    
    public boolean game(int[] piles, boolean alexTurn, int alexScore, int leeScore){
        if(piles.length == 1){
            if(alexTurn)
                return (alexScore + piles[0]) > leeScore;
            else
                return alexScore > (leeScore + piles[0]);
        } else if(alexTurn){
            return game(Arrays.copyOfRange(piles, 1, piles.length), false, alexScore+piles[0], leeScore) || game(Arrays.copyOfRange(piles,0,piles.length-1), false, alexScore+piles[piles.length-1], leeScore);
        } else{
            return game(Arrays.copyOfRange(piles, 1, piles.length), true, alexScore, leeScore+piles[0]) || game(Arrays.copyOfRange(piles,0,piles.length-1), true, alexScore, leeScore+piles[piles.length-1]);
        }
    }
    
    public boolean gameDP(int[] piles){
       int N = piles.length;

        // dp[i+1][j+1] = the value of the game [piles[i], ..., piles[j]].
        int[][] dp = new int[N+2][N+2];
        for (int size = 1; size <= N; ++size) {
            for (int i = 0; i + size <= N; ++i) {
                int j = i + size - 1;
                int parity = (j + i + N) % 2;  // j - i - N; but +x = -x (mod 2)
                if (parity == 1)
                    dp[i+1][j+1] = Math.max(piles[i] + dp[i+2][j+1], piles[j] + dp[i+1][j]);
                else
                    dp[i+1][j+1] = Math.min(-piles[i] + dp[i+2][j+1], -piles[j] + dp[i+1][j]);
            }
        }
        return dp[1][N] > 0;
    }
}