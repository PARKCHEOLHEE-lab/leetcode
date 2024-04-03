from typing import List

class Solution:
    """
        https://leetcode.com/problems/word-search/description/
        
        Given an m x n grid of characters board and a string word, return true if word exists in the grid.

        The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
        The same letter cell may not be used more than once.

        Constraints:
            m == board.length
            n = board[i].length
            1 <= m, n <= 6
            1 <= word.length <= 15
            board and word consists of only lowercase and uppercase English letters.

        Follow up: 
            Could you use search pruning to make your solution faster with a larger board?

    """
    
    def search(self, r, c, word_index):
        
        if word_index == len(self.word):
            return True
        
        if (
            r < 0
            or r >= self.row
            or c < 0
            or c >= self.col
            or (r, c) in self.visited
            or self.board[r][c] != self.word[word_index]
        ):
            return False
        
        self.visited.add((r, c))
        
        is_word_existing = (
            self.search(r, c + 1, word_index + 1)
            or self.search(r + 1, c, word_index + 1)
            or self.search(r, c - 1, word_index + 1)
            or self.search(r - 1, c, word_index + 1)
        )
        
        self.visited.remove((r, c))
            
        return is_word_existing
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.board = board
        self.word = word

        self.row = len(board)
        self.col = len(board[0])

        self.visited = set()
        
        for r in range(self.row):
            for c in range(self.col):
                if self.search(r, c, 0):
                    return True
        
        return False

if __name__ == "__main__":
    word = "ABCDEB"
    board = [
        ["A","B","E"],
        ["B","C","D"]
    ]
    assert Solution().exist(board, word) == True
    
    word = "bbbaabbbbbab"
    board = [
        ["a","a","b","a","a","b"],
        ["a","a","b","b","b","a"],
        ["a","a","a","a","b","a"],
        ["b","a","b","b","a","b"],
        ["a","b","b","a","b","a"],
        ["b","a","a","a","a","b"]
    ]
    assert Solution().exist(board, word) == False
    
    word = "ABCEFSADEESE"
    board = [
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]
    ]
    assert Solution().exist(board, word) == True

    word = "FCSE"
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    assert Solution().exist(board, word) == True
    
    word = "ABCCED"
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    assert Solution().exist(board, word) == True

    word = "SEE"
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    assert Solution().exist(board, word) == True

    word = "ABCB"
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    assert Solution().exist(board, word) == False