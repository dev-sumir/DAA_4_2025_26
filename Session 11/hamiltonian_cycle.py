v = 5

g = [
    [1,3],
    [0,2,3,4],
    [1,4],
    [0,1,4],
    [1,2,3]
]

p = [0]*v
vis = [False]*v

def edge(u,x):
    for i in g[u]:
        if i == x:
            return True
    return False

def go(u,c):
    if c == v:
        return edge(u,p[0])
    for i in g[u]:
        if not vis[i]:
            vis[i] = True
            p[c] = i
            if go(i,c+1):
                return True
            vis[i] = False
    return False

p[0] = 0
vis[0] = True

if go(0,1):
    for i in range(v):
        print(p[i], end=" ")
    print(p[0])
else:
    print("No cycle")
