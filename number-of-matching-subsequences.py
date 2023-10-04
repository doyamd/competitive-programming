class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endOfWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()     
        
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        d = defaultdict(int)
        def search(node,word,read):
            nonlocal count
            if node.endOfWord:
                count +=(d[read])
            for n in node.children:
                i = 0
                while i < len(word) and word[i] != n:
                    i += 1
                if i < len(word):
                    search(node.children[n],word[i+1:],read+n)
        for word in words:
            d[word] += 1
            dummy = self.root
            for w in word:
                if w not in dummy.children:
                    dummy.children[w] = TrieNode()
                dummy = dummy.children[w]
            dummy.endOfWord = True
        node = self.root
        search(node,s,"")
        return count