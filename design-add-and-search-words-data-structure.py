class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode() 

    def addWord(self, word: str) -> None:
        node = self.root
        self.main = word[0]
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node= node.children[letter]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        def search_dot(word,node):
            for i in range(len(word)):
                if word[i] == ".":
                    for char in node.children:
                        if search_dot(word[i+1:], node.children[char]):
                            return True
                elif word[i] not in node.children:
                    return False
                node = node.children[word[i]]
            return node.endOfWord
        return search_dot(word,self.root) 
                

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)