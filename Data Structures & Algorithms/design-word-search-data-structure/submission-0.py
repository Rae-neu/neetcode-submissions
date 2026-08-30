class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
        
            cur = cur.children[c]
        
        cur.isEnd = True

    def search(self, word: str) -> bool:    

        def dfs(index, node):
            if index == len(word):
                return node.isEnd
            
            c = word[index]

            if c != '.':
                if c not in node.children:
                    return False
                
                return dfs(index + 1, node.children[c])

            else:
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                
                return False
    
        return dfs(0, self.root)
            
