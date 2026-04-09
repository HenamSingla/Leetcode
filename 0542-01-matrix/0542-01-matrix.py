from collections import deque
class Solution:
    def updateMatrix(self, mat:List[List[int]])->List[List[int]]:
        #think about graphs
        #for 0, no need to do anything. for 1
        #i need to do bfs for 0
        rows,cols=len(mat),len(mat[0])
        queue=deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    queue.append((r,c))
                else:
                    mat[r][c]=float('inf')

        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols:
                    if mat[nr][nc]>mat[r][c]+1:
                        mat[nr][nc]=mat[r][c]+1
                        queue.append((nr,nc))
        return mat