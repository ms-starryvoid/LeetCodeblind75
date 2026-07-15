
class Trie:
    def __init__(self):
        self.children={}
        self.isend=False
class WordDictionary:

    def __init__(self):
        self.root=Trie()
        

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=Trie()
            cur=cur.children[c]
        cur.isend=True

        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.isend

            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            if c not in node.children:
                return False

            return dfs(i + 1, node.children[c])

        return dfs(0, self.root)