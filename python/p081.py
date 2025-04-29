# Find the minimal path sum from the top left to the bottom right by only moving right and down.
# Execution time: 0.233s

# f = open('inputs/p081_matrix.txt', 'r')

# matrix = []
# for line in f:
#     line = line.strip().split(',')
#     line = [int(d) for d in line]
#     matrix.append(line)


# for i in range(len(matrix) - 2, -1, -1):
#     matrix[len(matrix) - 1][i] += matrix[len(matrix) - 1][i+1]
#     matrix[i][len(matrix) - 1] += matrix[i+1][len(matrix) - 1]


# for i in range(len(matrix) - 2, -1, -1):
#     for j in range(len(matrix) - 2, -1, -1):
#         matrix[i][j] += min(matrix[i][j+1], matrix[i+1][j])


# print("Minimal sum", matrix[0][0])


import heapq

# Function to solve problem 83 using Dijkstra's algorithm
def minimal_path_sum(grid):
    n = len(grid)
    
    # Create a priority queue (min-heap) for Dijkstra's algorithm
    # Each entry is (cost, row, col)
    pq = []
    
    # Initialize the priority queue with the topleft element
    heapq.heappush(pq, (grid[0][0], 0, 0))  # (cost, row, col)
    
    # Create a distance table to store minimal cost to each cell
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = grid[0][0]  # Starting point
   
    # Directions for moving right and down
    directions = [(0, 1), (1, 0)]

    # Dijkstra's algorithm to find the minimal path sum
    while pq:
        current_dist, row, col = heapq.heappop(pq)
        
        # If we are in the bottom right we can check the result
        if row == n - 1 and col == n - 1:
            return current_dist
        
        # Explore all 4 possible neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n:
                # Calculate the new distance
                new_dist = current_dist + grid[new_row][new_col]
                # If a shorter path is found, update the distance table and push to the priority queue
                if new_dist < dist[new_row][new_col]:
                    dist[new_row][new_col] = new_dist
                    heapq.heappush(pq, (new_dist, new_row, new_col))
    
    # If the loop finishes, it means we found the minimal path sum
    return min(dist[n-1])  # Return the minimum value in the last row

# Example grid for Problem 83
grid = [[131, 673, 234, 103, 18],
          [201, 96, 342, 965, 150],
          [630, 803, 746, 422, 111],
          [537, 699, 497, 121, 956],
          [805, 732, 524, 37, 331]]

from numpy import transpose
grid = transpose(grid)

grid = []
with open("inputs/p081_matrix.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = list(map(int, line.strip().split(",")))
        grid.append(line)

# Solve the problem
result = minimal_path_sum(grid)
print(result)

# Priority Queue (Min-Heap): We will use a priority queue to always expand the cell with the smallest accumulated path sum.
# Distance Table: We will maintain a 2D array (dp) where dp[i][j] stores the minimal cost to reach cell (i, j).

if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
