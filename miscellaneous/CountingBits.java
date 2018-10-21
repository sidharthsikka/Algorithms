class CountingBits {
    public int[] countBits(int num) {
        int[] result = new int[num+1];
        if(num == 0){
            result[0] = 0;
            return result;
        }
        int max = 1;
        result[0] = 0;
        result[1] = 1;
        for(int i=2;i<=num;i++){
            if(i == max * 2){
                result[i] = 1;
                max *= 2;
            } else{
                result[i] = 1 + result[i-max];
            }
        }
        return result;
    }
}