public class Solution
{
    public int SwimInWater(int[][] grid) {
        var path = new Dictionary<(int, int), int>{};
        int n = grid.Length;
        for (int i = 0; i< n; i++)
        {
            for (int j =0; j < n; j++)
            {
                path.Add((i, j), -1);
            }
        }
        (int, int) select_index = (0, 0); 
        path[select_index] = grid[select_index.Item1][select_index.Item2];
        (int, int)[] sides = [(1, 0), (0,1),(-1,0), (0,-1)];
        while(!(select_index.Item1 == n - 1 && select_index.Item2 == n - 1))
        {

            foreach (var side in sides)
            {   
                var (x, y) = select_index;
                x += side.Item1;
                y += side.Item2;
                if (x < n && x >= 0 && y < n && y >= 0)
                {
                    int item_value;
                    int table_value = grid[x][y];
                    if (path.TryGetValue((x, y), out item_value))
                    {
                        if (table_value > path[select_index])
                        {
                            path[(x,y)] = table_value;
                        }
                        else
                        {
                            path[(x,y)] = path[select_index];
                        }
                    }
                }
            }
            path.Remove(select_index);
            int min_value = int.MaxValue;
            foreach (var (key, value) in path)
            {   
                if (value >= 0 && value < min_value)
                {
                    min_value = value;
                    select_index = key;
                }
            }
        }
        return path[(n-1,n-1)];
    }
    
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        int[][] grid = [[0,3],[1,2]];
        Console.WriteLine(solution.SwimInWater(grid));

        
    }
}
