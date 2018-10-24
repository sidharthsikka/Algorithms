class QueueReconstructionByHeight implements Comparator<int[]> {
    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, new Solution());
        List<int[]> temp = new ArrayList<>();
        int[][] res = new int[people.length][2];
        for(int i=0;i<people.length;i++){
            temp.add(people[i][1], people[i]);
        }
        int i = 0;
        for(int[] x : temp){
            res[i] = x;
            i++;
        }
        return res;
    }
    
    @Override
    public int compare(int[] x1, int[] x2){
        if (x1[0] == x2[0])
            return x1[1] - x2[1];
        return x2[0] - x1[0];
    }
}