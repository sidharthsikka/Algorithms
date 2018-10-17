class StringToInt {
    public int myAtoi(String str) {
        int index = 0;
        int result = 0;
        boolean negative = false;
        int size = str.length();
        while(index<size && str.charAt(index) == ' '){
            index++;
        }
        if(index<size && str.charAt(index) == '-'){
            index++;
            negative = true;
        } else if(index<size && str.charAt(index) == '+'){
            index++;
        }
        while(index<size && str.charAt(index)>= '0' && str.charAt(index) <= '9'){
            long temp = ((long)result * 10) + Character.getNumericValue(str.charAt(index));
            if(temp > Integer.MAX_VALUE){ //overflow has occured
                if(negative)
                    return Integer.MIN_VALUE;
                return Integer.MAX_VALUE;
            }
            result = (int)temp;
            index++;
        }
        if(negative){
            return result * -1;
        }
        return result;
    }
}