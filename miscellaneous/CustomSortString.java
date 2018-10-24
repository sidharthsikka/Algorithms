class CustomSortString {
    public String customSortString(String S, String T) {
        StringBuilder result = new StringBuilder("");
        Map<Character,Integer> charToFreq = new HashMap<>();
        for(int i=0;i<T.length();i++){
            if(charToFreq.containsKey(T.charAt(i))){
                int count = charToFreq.get(T.charAt(i));
                count++;
                charToFreq.put(T.charAt(i), count);
            } else{
                charToFreq.put(T.charAt(i), 1);
            }
        }
        for(int i=0;i<S.length();i++){
            if(charToFreq.containsKey(S.charAt(i))){
                for(int j=0;j<charToFreq.get(S.charAt(i));j++){
                    result.append(S.charAt(i));
                }
                charToFreq.remove(S.charAt(i));
            }
        }
        for(Map.Entry<Character, Integer> x : charToFreq.entrySet()){
            for(int j=0;j<x.getValue();j++){
                result.append(x.getKey());
            }
        }
        return result.toString();
    }
}