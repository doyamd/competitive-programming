class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:    
        d = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        for i in range(len(ingredients)):
            for j in ingredients[i]:
                graph[j].append(recipes[i])
        for i in range(len(recipes)):
            d[recipes[i]] += len(ingredients[i])
        for i in supplies:
            queue.append(i)
        ans = []
        while queue and len(ans) != len(recipes):
            
            inger = queue.popleft()
            if inger in recipes:
                ans.append(inger)
            for i in graph[inger]:
                d[i] -= 1
                if not d[i]:
                    queue.append(i)
            
        return ans