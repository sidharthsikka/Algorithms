class FindAndReplacePattern {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> result = new ArrayList<>();
        boolean place = true;
        for(int i=0;i<words.length;i++){
            String word = words[i];
            List<Character> letterW = new ArrayList<>();
            List<Character> letterP = new ArrayList<>();
            for(int j=0;j<word.length();j++){
               if(letterP.contains(pattern.charAt(j)) && letterW.get(letterP.indexOf(pattern.charAt(j))) == word.charAt(j)){
                   continue;
               } else if(!letterP.contains(pattern.charAt(j)) && !letterW.contains(word.charAt(j))){
                   letterW.add(word.charAt(j));
                   letterP.add(pattern.charAt(j));
               } else {
                   place = false;
                   break;
               }
            }
            if(place){
                result.add(words[i]);
            }
            place = true;
        }
        return result;
    }
}