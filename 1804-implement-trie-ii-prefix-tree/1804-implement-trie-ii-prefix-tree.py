class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.wordCount = 0
        self.prefixCount = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.children[letter]
            current.prefixCount += 1
        current.wordCount += 1

    def countWordsEqualTo(self, word: str) -> int:
        current = self.root
        for letter in word:
            if letter not in current.children:
                return 0
            else:
                current = current.children[letter]
        return current.wordCount

    def countWordsStartingWith(self, prefix: str) -> int:
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return 0
            else:
                current = current.children[letter]
        return current.prefixCount
            

    def erase(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.children[letter]
            current.prefixCount -= 1
        current.wordCount -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)