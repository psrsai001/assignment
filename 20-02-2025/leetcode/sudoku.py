class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = {(i // 3, j // 3): set() for i in range(9) for j in range(9)}

        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    ele = board[i][j]
                    rows[i].add(ele)
                    cols[j].add(ele)
                    grid[(i // 3, j // 3)].add(ele)
                else:
                    empty_cells.append((i, j))

        def backtrack(index):
            if index == len(empty_cells):
                return True

            i, j = empty_cells[index]
            key = (i // 3, j // 3)

            for ele in "123456789":
                if ele not in rows[i] and ele not in cols[j] and ele not in grid[key]:
                    # Place the number
                    board[i][j] = ele
                    rows[i].add(ele)
                    cols[j].add(ele)
                    grid[key].add(ele)

                    if backtrack(index + 1):
                        return True
                    board[i][j] = "."
                    rows[i].remove(ele)
                    cols[j].remove(ele)
                    grid[key].remove(ele)

            return False

        backtrack(0)
