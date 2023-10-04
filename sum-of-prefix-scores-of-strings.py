class TrieNode:
    def __init__(self):
        self.children ={}
        self.endOfWord = False
        self.count = 0
    def insert(self,word):
        dummy = self
        for w in word:
            if w not in dummy.children:
                dummy.children[w] = TrieNode()
            dummy = dummy.children[w]
            dummy.count += 1
            # print(w,dummy.count)
        dummy.endOfWord = True
    def search(self,word):
        node= self
        count = 0
        for char in word:
            # print(char,node.count)
            count += node.children[char].count
            node = node.children[char]
        return count

    

class Solution:
    def __init__(self):
        self.root = TrieNode()  
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = []
        for word in words:
            self.root.insert(word)
        for word in words:
            ans.append(self.root.search(word))
        return ans