class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    d[board[i][j]].append([i,j])
        for c,v in d.items():
            for x in v:
                frLinie=[0]*10
                frColoana=[0]*10
                frPatrat=[[0]*3 for _ in range(3)]
                for i,j in v:
                    if frLinie[i]!=0 or frColoana[j]!=0 or frPatrat[i//3][j//3]!=0:
                        return False
                    frLinie[i]+=1
                    frColoana[j]+=1
                    frPatrat[i//3][j//3]+=1
        return True
