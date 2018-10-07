/*Given a turtle on the left-bottom corner who can move only
right or up. Each cell has a cost.
Find the minimal path to the opposite corner.*/


public class  min_path_to_opposite_corner {
    public static void main(String[] args){
        
    }

    public static int min_path(int[][] grid){
        int[][] min_grid = new int[grid.length][grid[0].length];
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if( i == 0 && j == 0)
                    min_grid[i][j] = grid[0][0];
                else
                    min_grid[i][j] = Integer.MAX_VALUE;
            }
        }
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(i+1<grid.length && min_grid[i+1][j] > min_grid[i][j] + grid[i+1][j]){
                    min_grid[i+1][j] = min_grid[i][j] + grid[i+1][j];
                }
                if(j+1<grid[0].length && min_grid[i][j+1] > min_grid[i][j] + grid[i][j+1]){
                    min_grid[i][j+1] = min_grid[i][j] + grid[i][j+1];
                }
            }
        }
        return min_grid[grid.length-1][grid[0].length-1];
    }
}