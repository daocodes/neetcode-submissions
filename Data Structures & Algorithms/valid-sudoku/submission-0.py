class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # r = 3, c = 0
        # (r // 3 )*3 + (c // 3)


        rowDict = collections.defaultdict(set)
        colDict = collections.defaultdict(set)
        gridDict = collections.defaultdict(set)


        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue


                gridIdx = 3*(r//3) + (c // 3)

                if (board[r][c] in rowDict[r]) or (board[r][c] in colDict[c])  or (board[r][c] in gridDict[gridIdx]):
                    return False


                rowDict[r].add(board[r][c])
                colDict[c].add(board[r][c])
                gridDict[gridIdx].add(board[r][c])


        return True


                

        