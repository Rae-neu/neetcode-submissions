class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        self.root = TrieNode()

        for word in words:
            cur = self.root
            for w in word:
                if w not in cur.children:
                    cur.children[w] = TrieNode()
                    
                cur = cur.children[w]
            cur.isEnd = True

        def dfs(row, col, node, path):
            if row < 0  or row >= len(board) or col < 0 or col >= len(board[0]):
                return
            
            if board[row][col] == '#':
                return
            
            c = board[row][col]

            if c not in node.children:
                return

            node = node.children[c]
            path.append(c)

            if node.isEnd == True:
                result.append(''.join(path))
                node.isEnd = False
            
            board[row][col] = '#'

            dfs(row-1, col, node, path)
            dfs(row+1, col, node, path)
            dfs(row, col+1, node, path)
            dfs(row, col-1, node, path)

            board[row][col] = c
            path.pop()
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, self.root, [])
                
        return result


            


                