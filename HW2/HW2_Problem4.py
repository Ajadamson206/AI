# 
#   Albert Adamson
#   Problem 4: Number of Islands
#   
#   Note: This is the same code found in the screenshot, the only difference is that I added comments + the headers
#   so it could be ran locally on my machine.
#
#   Explanation:
#   The algorithm for Problem 4 works by looping through the grid until an island ("1") is found. 
#   Then once an island is found we use BFS to search through the entire island until all pieces of land have been marked. 
#   Additionally, everytime we reach a piece of land, we add it to the set, "visited", so we don't count the same island multiple times.
#

from typing import *
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        # Loop Through Both the Rows and Columns
        for rowNum, row in enumerate(grid):
            for colNum, value in enumerate(row):

                # Ignore the nodes that we have already visited
                if ((rowNum, colNum) in visited):
                    continue
            
                # Island Detected
                if value == "1":
                    self.bfs(grid, visited, rowNum, colNum)
                    count += 1
    
        return count
    
    def bfs(self, grid: List[List[str]], visited: set, row: int, column: int):
        q = deque()
        q.append((row, column))
        visited.add((row, column))

        # Continue until the queue is empty
        while len(q) != 0:
            orderedPair = q.popleft()

            # Add north value to the queue, check if it is valid and hasn't been visited
            north = (orderedPair[0] - 1, orderedPair[1])
            if north[0] >= 0 and north not in visited and grid[north[0]][north[1]] == "1":
                visited.add(north)
                q.append(north)

            # Add east value to the queue, check if it is valid and hasn't been visited
            east = (orderedPair[0], orderedPair[1] + 1)
            if east[1] < len(grid[0]) and east not in visited and grid[east[0]][east[1]] == "1":
                visited.add(east)
                q.append(east)

            # Add west value to the queue, check if it is valid and hasn't been visited
            west = (orderedPair[0], orderedPair[1] - 1)
            if west[1] >= 0 and west not in visited and grid[west[0]][west[1]] == "1":
                visited.add(west)
                q.append(west)

            # Add south value to the queue, check if it is valid and hasn't been visited
            south = (orderedPair[0] + 1, orderedPair[1])
            if south[0] < len(grid) and south not in visited and grid[south[0]][south[1]] == "1":
                visited.add(south)
                q.append(south)


