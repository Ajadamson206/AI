#
#   Albert Adamson
#   Homework 3 - Problem 4
#   10/21/25
#

#   Note this is the same code as the LeetCode SS, just with added comments
#
#   This solution used a priority queue following Dijkstra's shortest path algorithm.
#   In the solution, for each movement against the arrow I added 1 to the value of the node which 
#   was being tracked inside of the values dictionary. If the node was in the same direction
#   as the arrow it didn't get 1 added to it's value. I continued this until I reached the goal node, and since
#   the priority queue always has the smallest number first, once the goal node was reached I was certain
#   that it was the path which costed the least.
#

from queue import PriorityQueue     # This import is required in LeetCode
from typing import List             # This import is not required, just removes warnings

class Solution:
    # Which Direction is the Arrow Pointing
    def specialDirection(self, number: int):
        if number == 1:
            return (0,1)
        elif number == 2:
            return (0,-1)
        elif number == 3:
            return (1, 0)
        else:
            return (-1, 0)

    # Main Solution
    def minCost(self, grid: List[List[int]]) -> int:
        # Calculate Goal and Bounds
        max_x = len(grid)
        max_y = len(grid[0])
        
        goalx, goaly = max_x - 1, max_y - 1
        start = (0,0)
        
        # Use a priority queue f(n) = g(n)
        queue = PriorityQueue()
        
        # Keep track of visited nodes plus their values
        values = {}

        queue.put((0, start))
        values.update({(0,0): 0})
        while not queue.empty():
            # Pop node off of queue, and get position
            current_cost, current_pos = queue.get()
            current_cell = grid[current_pos[0]][current_pos[1]]

            # Check Win Condition
            if goalx == current_pos[0] and goaly == current_pos[1]:
                return current_cost
            
            # Which direction is the free movement
            special_direction = self.specialDirection(current_cell)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_pos = (current_pos[0] + dx, current_pos[1] + dy)
                
                # Check Bounds
                if (0 <= new_pos[0] < max_x) and 0 <= new_pos[1] < max_y:
                    new_g = 0
                    # G does NOT update if we move in the arrow's direction
                    if dx == special_direction[0] and dy == special_direction[1]:
                        new_g = current_cost
                    else:
                        new_g = current_cost + 1

                    # Check if the node has been visited or we found a faster path
                    if values.get((current_pos[0] + dx, current_pos[1] + dy)) == None or values.get((current_pos[0] + dx, current_pos[1] + dy)) > new_g:
                        # Update the node / Add it to the queue
                        values.update({(current_pos[0] + dx, current_pos[1] + dy): new_g})
                        queue.put((new_g, (current_pos[0] + dx, current_pos[1] + dy)))
        
        # Should never reach here
        return 0


