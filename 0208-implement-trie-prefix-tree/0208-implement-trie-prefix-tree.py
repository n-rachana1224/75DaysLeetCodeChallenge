class TrieNode(object):
    __slots__ = ["children", "is_end"]

    def __init__(self):
        self.children = [None] * 26  # a-z
        self.is_end = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def _idx(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        node = self.root
        for ch in word:
            i = self._idx(ch)
            if node.children[i] is None:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            i = self._idx(ch)
            if node.children[i] is None:
                return False
            node = node.children[i]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            i = self._idx(ch)
            if node.children[i] is None:
                return False
            node = node.children[i]
        return True