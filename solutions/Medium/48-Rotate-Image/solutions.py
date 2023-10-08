class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        n = len(mat)
        for i in range(int(n/2)):
            for j in range(i,n-1-i):
                temp = mat[i][j]
                mat[i][j] = mat[n-j-1][i]
                mat[n-j-1][i] = mat[n-i-1][n-j-1]
                mat[n-i-1][n-j-1] = mat[j][n-i-1]
                mat[j][n-i-1] = temp
        return mat