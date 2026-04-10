class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        q = deque()
        q.append((src, 0))
        
        dist = [float('inf')] * n
        dist[src] = 0
        
        stops = 0
        
        while q and stops <= k:
            size = len(q)
            temp = dist[:]
            
            for _ in range(size):
                node, cost = q.popleft()
                
                for nei, price in graph[node]:
                    if cost + price < temp[nei]:
                        temp[nei] = cost + price
                        q.append((nei, cost + price))
            
            dist = temp
            stops += 1
        
        return -1 if dist[dst] == float('inf') else dist[dst]
