class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word) :
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word) :

        def dfs(i, node):
            for j in range(i, len(word)):
                ch = word[j]

                # Case 1: wildcard
                if ch == '.':
                    for child in node.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False

                # Case 2: normal character
                if ch not in node.children:
                    return False

                node = node.children[ch]

            return node.end

        return dfs(0, self.root)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)