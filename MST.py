class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# KRUSKAL MST class inspired by "geeks for geeks" written by myself
class MST: 
    def __init__(self,v):
         self.graph = []
         self.vertices = v

    def add_edge(self,src, dest, weight):
        self.graph.append([src, dest, weight])

    def find(self, parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return  self.find(parent, parent[vertex])
                        
    def union(self, parent, rank, vertex_x, vertex_y):
        x_set =  self.find(parent, vertex_x)
        y_set =  self.find(parent, vertex_y)

        if rank[x_set] < rank[y_set]:
            parent[x_set] = y_set
        elif rank[x_set] > rank[y_set]:
            parent[y_set] = x_set
        else:
            parent[y_set] = x_set
            rank[x_set] += 1

    def get_mst_weight(self):
        self.graph = sorted(self.graph, key=lambda edge: edge[2])

        parent = {}
        rank = {}
        for vertex in self.vertices:
            parent[vertex] = vertex
            rank[vertex] = 0

        edge_count = 0
        mst_weight  = 0
        num_mst_edges = 0

        while num_mst_edges < len(self.vertices) - 1:
            src, dest, weight = self.graph[edge_count]
            edge_count += 1
            src_set =  self.find(parent, src)
            dest_set =  self.find(parent, dest)

            if src_set != dest_set:
                num_mst_edges += 1
                mst_weight += weight
                self.union(parent, rank, src, dest)

        return mst_weight