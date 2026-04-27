class Solution:
    def dijkstra(self, V, edges, src):
        adj=[[] for _ in range(V)]
        
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
            
        dist = [float('inf')]*V
        dist[src]=0
        
        pq=[(0,src)]
        while pq:
            d,node = heapq.heappop(pq)
            
            if d>dist[node]:
                continue
            
            for nei,wt in adj[node]:
                if dist[node]+wt < dist[nei]:
                    dist[nei]=dist[node]+wt
                    heapq.heappush(pq,(dist[nei],nei))
                    
        return dist
