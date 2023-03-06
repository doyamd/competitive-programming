class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        query_len = []
        word_len = []
        ans = []
        length_w = len(words)
        for que in queries:
            query_len.append(que.count(min(que)))
        for wor in words:
            word_len.append(wor.count(min(wor)))
        word_len.sort()
        for q in query_len :
            num = length_w - bisect.bisect_right(word_len,q)
            ans.append(num)
        return ans