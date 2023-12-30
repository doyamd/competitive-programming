class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        length = len(words)
        if length == 1:
            return True
        new_word = ''.join(words)
        counted = Counter(new_word)
        for k,v in counted.items():
            if v % length != 0:
                return False
        return True
        
