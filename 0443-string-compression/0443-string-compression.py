class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        length = 0
        while i < len(chars) and j < len(chars):
            count = 1
            while j < len(chars)-1 and chars[j] == chars[j + 1] :
                count += 1
                j += 1
            
            chars[i] = chars[j]
            length += 1
            if count > 1:
                for x in str(count):
                    i += 1
                    chars[i] = x
                    length += 1
            i += 1
            j += 1
        return length