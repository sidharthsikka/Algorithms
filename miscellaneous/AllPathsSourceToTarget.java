class AllPathsSourceToTarget {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int nodes = graph.length;
        List<List<List<Integer>>> dp_result = new ArrayList<>(nodes);
        for(int i=0;i<nodes;i++){
            List<List<Integer>> x = new ArrayList<>();
            dp_result.add(x);
        }
        List<List<Integer>> start = new ArrayList<>(1);
        List<Integer> starting_node = new ArrayList<>(1);
        starting_node.add(0);
        start.add(starting_node);
        dp_result.add(0, start);
        for(int i=0;i<nodes;i++){
            List<List<Integer>> base = new ArrayList<>(dp_result.get(i));
            int[] neighbours = graph[i];
            for(int j=0;j<neighbours.length;j++){
                int node = neighbours[j];
                List<List<Integer>> extension = new ArrayList<>();
                for(int k=0;k<base.size();k++){
                    List<Integer> temp = new ArrayList<>(base.get(k));
                    temp.add(node);
                    extension.add(temp);
                }
                dp_result.get(node).addAll(extension);
            }
        }
        return dp_result.get(nodes-1);
    }
}