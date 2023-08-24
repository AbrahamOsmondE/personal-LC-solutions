class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = [[10001 for j in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    if i > 0:
                        dist[i][j] = min(dist[i][j],dist[i-1][j]+1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j],dist[i][j-1]+1)
                else:
                    dist[i][j] = 0
                    
        
        for i in range(len(mat)-1,-1,-1):
            for j in range(len(mat[0])-1,-1,-1):
                if mat[i][j] != 0:
                    if j < len(mat[0])-1:
                        dist[i][j] = min(dist[i][j],dist[i][j+1]+1)
                    if i < len(mat)-1:
                        dist[i][j] = min(dist[i][j],dist[i+1][j]+1)
                else:
                    dist[i][j] = 0
                    
        return dist
        
                    