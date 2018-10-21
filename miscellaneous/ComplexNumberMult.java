class ComplexNumberMult {
    public String complexNumberMultiply(String a, String b) {
        int[] nums = new int[4];
        String[] temp = a.split("\\+");
        temp[1] = temp[1].substring(0, temp[1].length()-1);
        for(int i=0;i<2;i++){
            nums[i] = Integer.parseInt(temp[i]);   
        }
        temp = b.split("\\+");
        temp[1] = temp[1].substring(0, temp[1].length()-1);
        for(int i=0;i<2;i++){
            nums[i+2] = Integer.parseInt(temp[i]);   
        }
        return ((nums[0] * nums[2]) + (nums[1] * nums[3] * -1)) + "+" + ((nums[0] * nums[3]) + (nums[1] * nums[2])) + "i";
    }
}