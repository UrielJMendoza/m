class WordDictionary:

    def __init__(self):
        self.children = {}
        self.word = False
        

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.word = True


    def search(self, word: str) -> bool:
        return self.dfs(self, word, 0)


    def dfs(self, node, word, i):
        if i == len(word):
            return node.word
        c = word[i]
        if c == ".":
            for child in node.children.values():
                if self.dfs(child, word, i + 1):
                    return True
            return False
        if c not in node.children:
            return False
        return self.dfs(node.children[c], word, i + 1)