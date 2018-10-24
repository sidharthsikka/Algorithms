class CountBinaryStrings {
    public int countBinarySubstrings(String s) {
        int res = 0;
        int i = 1;
        List<Tuple> collapsed = new ArrayList<>();
        Tuple curr = new Tuple(s.charAt(0), 1);
        collapsed.add(curr);
        while(i < s.length()){
            if(s.charAt(i) == curr.getLetter()){
                curr.increment();
            } else {
                curr = new Tuple(s.charAt(i), 1);
                collapsed.add(curr);
            }
            i++;
        }
        for(i=0;i<collapsed.size()-1;i++){
            if(collapsed.get(i).getCount() <= collapsed.get(i+1).getCount())
                res += collapsed.get(i).getCount();
            else
                res += collapsed.get(i+1).getCount();
        }
        return res;
    }
    
    class Tuple {
        private final char letter;
        private int count;
        
        public Tuple(char letter, int count){
            this.letter = letter;
            this.count = count;
        }
        
        public void increment(){ count++; }
        
        public int getCount(){ return this.count; }
        
        public char getLetter(){ return this.letter; }
    }
}