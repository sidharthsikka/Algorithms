class ReverseInt {
    public int reverse(int x) {
        int result = 0;
        while(x != 0){
            long temp = ((long)result * 10) + x%10;
            if(temp > Integer.MAX_VALUE || temp < Integer.MIN_VALUE) { //Overflow
                return 0;
            }
            result = (int)temp;
            x/=10;
        }
        return result;
    }
}