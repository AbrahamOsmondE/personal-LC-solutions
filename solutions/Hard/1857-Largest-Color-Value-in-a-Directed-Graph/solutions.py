from collections import defaultdict, deque
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        
        # Map the colors from str to int
        color_map = {}
        for c in colors:
            if c not in color_map:
                color_map[c] = len(color_map)
        color_size = len(color_map)
        
        # Construct the graph with adj list and calc the in degree of each node
        neighbor = defaultdict(lambda: [])
        deg = [0 for i in range(n)]
        for a, b in edges:
            neighbor[a].append(b)
            deg[b] += 1
        
        # Topological Sorting and Dynamic Programming
        queue = deque()
        
        # Each node has a list. The ith element represents
        # the maximum number of nodes with ith color in the paths that 
        # has been found so far.
        dp = defaultdict(lambda: [0 for i in range(color_size)])
        
        for i in range(n):