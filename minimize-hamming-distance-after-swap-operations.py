class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        parent = {i: i for i in range(len(source))}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for x, y in allowedSwaps:
            parent[find(x)] = find(y)
        
        
        components = defaultdict(list)
        for i in range(len(source)):
            root = find(i)
            components[root].append(i)
        
        
        dis = 0
        for component in components.values():
            sc = defaultdict(int)
            tc = defaultdict(int)
            for index in component:
                sc[source[index]] += 1
                tc[target[index]] += 1
            for num, count in sc.items():
                dis += min(count, tc[num])
        
        return len(source) - dis