class LongestPalindromicSubstring {
    public String longestPalindrome(String s) {
        int len = s.length();
        String res = "";
        boolean[][] dp = new boolean[len][len];
        for(int size=0;size<len;size++){
            for(int i=0;i<len-size;i++){
                int j = i + size;
                if(i+1 < j-1) {
                    dp[i][j] = dp[i+1][j-1] && s.charAt(i) == s.charAt(j);
                } else {
                    dp[i][j] = s.charAt(i) == s.charAt(j);
                }
                if(dp[i][j] && size+1 > res.length()){
                    res = s.substring(i, j+1);
                }
            }
        }
        return res;
    }
}