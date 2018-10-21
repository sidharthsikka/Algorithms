class PartitionLabels {
    public List<Integer> partitionLabels(String S) {
        List<Integer> result = new ArrayList<Integer>();
        List<Tuple> y = new ArrayList<Tuple>();
        boolean added = false;
        List<Character> chars = new ArrayList<>();
        List<Tuple> tuples = new ArrayList<>();
        for(int i=0;i<S.length();i++){
            char c = S.charAt(i);
            if(chars.contains(c)){
                Tuple temp = tuples.get(chars.indexOf(c));
                temp.setEnd(i);
            } else{
                Tuple temp = new Tuple(i,i);
                chars.add(c);
                tuples.add(temp);
            }
        }
        for(Tuple ex : tuples){
            Tuple toRemove = null;
            for(Tuple res : y){
                if((ex.getStart() >= res.getStart() && ex.getStart() <= res.getEnd())
                  || (ex.getEnd() >= res.getStart() && ex.getEnd() <= res.getEnd())
                  || (ex.getStart() < res.getStart() && ex.getEnd() > res.getEnd())){
                    y.add(new Tuple(Math.min(ex.getStart(), res.getStart()), Math.max(ex.getEnd(), res.getEnd())));
                    added = true;
                    toRemove = res;
                    break;
                }
            }
            if(!added){
                y.add(ex);
            }
            if(toRemove != null)
                y.remove(toRemove);
            added = false;
            toRemove = null;
        }
        for(Tuple x: y){
            result.add(x.getEnd() - x.getStart() + 1);
        }
        return result;
    }
    
    class Tuple {
        private int start;
        private int end;
        
        public Tuple(int start, int end){
            this.start = start;
            this.end = end;
        }
        
        public int getStart(){ return this.start; }
        
        public int getEnd(){ return this.end; }
        
        public void setStart(int start){ this.start = start; }
        
        public void setEnd(int end){ this.end = end; }
    }
}