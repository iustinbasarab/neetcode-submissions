class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = defaultdict(list) 
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                   d[board[i][j]].append([i, j])
        for cifra, pozitii in d.items():
            frlinii = [0]*10
            frcoloane = [0]*10
            frpatrat = [[0]*10 for _ in range(9)]
            for i, j in pozitii:
                if frlinii[i] != 0 or frcoloane[j] != 0 or frpatrat[i//3][j//3] != 0:
                    return False
                frlinii[i]+=1
                frcoloane[j]+=1
                frpatrat[i//3][j//3] += 1
        return True
                
                

            
    