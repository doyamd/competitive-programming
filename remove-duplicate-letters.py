class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = Counter(s)
        stack = []
        i = 0
        while i < len(s):
            if not stack:
                stack.append(s[i])
            elif stack and s[i] not in stack and stack[-1] < s[i]:
                stack.append(s[i])
            elif stack and stack[-1] > s[i] and d[stack[-1]] > 1 and s[i] not in stack:
                while stack and stack[-1] > s[i] and d[stack[-1]] > 1 :
                    d[stack[-1]] -= 1
                    stack.pop()
                if s[i] not in stack:
                    stack.append(s[i])
            elif s[i] not in stack:
                stack.append(s[i])
            elif s[i] in stack:
                d[s[i]] -= 1
            print(stack)
            i += 1

        return "".join(stack)