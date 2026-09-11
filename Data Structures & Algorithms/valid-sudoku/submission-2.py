class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqaure = collections.defaultdict(set)     
        ##make a hash set for each rows and cols and 3x3 sqaure



        
        for r in range(len(board)):
            for c in range(len(board)):
                ##loop through all fors and cols
                if board[r][c] == ".":
                    ##if nothing in the board for r and c then continue no need to check
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sqaure[r//3, c // 3]:
                    return False##if something in the hashset and in the baord then we have to return flase so it check the row for duplicates and the colums then it also check the sqaure 3x3 if there is any duplicates 
                cols[c].add(board[r][c])##if no duplicates then we add the current calues into our seen  for both collums and rows

                rows[r].add(board[r][c])
                sqaure[(r//3, c // 3)].add(board[r][c])### if no duplicates then we add the current values to the 3x3 matrix
        return True ##if we go through the whole thing and no dups return true

                



                