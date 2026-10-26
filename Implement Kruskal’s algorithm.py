def kruskal(vertices, edges):
    parent = {v: v for v in vertices}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)

        if root_u != root_v:
            parent[root_v] = root_u
            return True
        return False

    edges.sort(key=lambda edge: edge[2])
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    if len(mst) != len(vertices) - 1:
        print("Graph is not connected!")
        return

    print("Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(u, "-", v, ":", weight)

    print("Total Cost:", total_cost)


vertices = ['A', 'B', 'C', 'D']

edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 5)
]

kruskal(vertices, edges)
