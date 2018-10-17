class BestTimeBuyAndSellStock {
    public int maxProfit(int[] prices) {
        int result = 0;
        int buyingPrice = Integer.MAX_VALUE;
        for(int i=0;i<prices.length;i++){
            if(prices[i] < buyingPrice){
                buyingPrice = prices[i];
            } else if(prices[i] - buyingPrice > result){
                result = prices[i] - buyingPrice;
            }
        }
        return result;
    }
}