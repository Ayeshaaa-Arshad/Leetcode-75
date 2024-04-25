#Solution 1
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_hash = []
        result = 0

        for i in range(len(grid)):
            row_hash.append(hash(tuple(grid[i])))

        transposed_matrix = list(zip(*grid))

        for i in range(len(transposed_matrix)):
            hashed_column = hash(tuple(transposed_matrix[i]))
            if hashed_column in row_hash:
                result += row_hash.count(hashed_column)
        return result

#Solution 2
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_hash = []
        result = 0

        for row in grid:
            row_hash.append(hash(tuple(row)))

        # Iterate over the grid, considering each column as needed
        for j in range(len(grid[0])):
            col_hash = hash(tuple(grid[i][j] for i in range(len(grid))))
            result += row_hash.count(col_hash)

        return result

sol = Solution()
print(sol.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
