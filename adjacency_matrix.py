class Graph:
    def __init__(self, numvertex):
        self.adjmatrix = [[-1]*numvertex for i in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = {}
        self.verticeslist = [0]*numvertex
    def set_vertex(self, vertex, id):
        if 0<=vertex<=self.numvertex:
            self.vertices[id] = vertex
            self.verticeslist[vertex] = id
    def set_edge(self,frm,to,cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjmatrix[frm][to] = cost
        #directed graph
        self.adjmatrix[to][frm] = cost
    def get_vertex(self):
        return self.verticeslist
    def get_edges(self):
        edges = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if self.adjmatrix[i][j]!=-1:
                    edges.append(self.verticeslist[i],self.verticeslist[j],self.adjmatrix[i][j])
        return edges
    def get_matrix(self):
        return self.adjmatrix

g = Graph(6)
g.set_vertex(0,"s")
g.set_vertex(1,"e")
g.set_vertex(2,"l")
g.set_vertex(3,"c")
g.set_vertex(4,"i")
g.set_vertex(5,"a")
print(g.get_vertex())
g.set_edge("s","e",4)
print(g.get_edges())