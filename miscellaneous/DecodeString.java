// The encoding rule is: k[encoded_string], where the encoded_string 
// inside the square brackets is being repeated exactly k times. 

class DecodeString {
    public String decodeString(String s) {
        StringBuilder result = new StringBuilder("");
        Stack<Tups> stack = new Stack<>();
        for(int i=0;i<s.length();i++){
            if('0' <= s.charAt(i) && s.charAt(i) <= '9'){
                StringBuilder number = new StringBuilder("");
                while(s.charAt(i) != '['){
                    number.append(s.charAt(i));
                    i++;
                }
                Tups temp = new Tups(Integer.parseInt(number.toString()));
                stack.push(temp);
            } else if(('a' <= s.charAt(i) && s.charAt(i) <= 'z') || ('A' <= s.charAt(i) && s.charAt(i) <= 'Z')){
                if(!stack.empty()){
                    Tups temp = stack.peek();
                    temp.appendLetter(s.charAt(i));
                } else{
                    result.append(s.charAt(i));
                }
            } else if(s.charAt(i) == ']'){
                Tups t = stack.pop();
                System.out.println(t.getCount() + " " + t.getString());
                if(!stack.empty()){
                    Tups temp = stack.peek();
                    for(int j=0;j<t.getCount();j++){
                        temp.appendString(t.getString());
                    }
                } else {
                    for(int j=0;j<t.getCount();j++){
                        result.append(t.getString());
                    }
                }
            }
        }
        return result.toString();
    }
    
    class Tups{
        private int count;
        private StringBuilder string;
        
        public Tups(int count){
            this.count = count;
            this.string = new StringBuilder("");
        }
        
        public int getCount(){ return this.count; }
        
        public String getString() { return this.string.toString(); }
        
        public void appendLetter(char c){ this.string.append(c); }
        
        public void appendString(String s){ this.string.append(s); }
    }
}