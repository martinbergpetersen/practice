class Edge:
    def __init__(self, from_, to):
        self.from_ = from_
        self.to = to

    def reversed(self):
        return Edge(self.to, self.from_)

    def __str__(self):
        return f'{self.from_} -> {self.to}'


class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = [[] for _ in vertices]

    @property
    def vertex_count(self):
        return len(self._vertices)

    @property
    def edge_count(self):
        edge_len = [len(edge) for edge in self._edges]
        return sum(edge_len)

    def add_vertex(self, vertex):
        """Add a vertex to the graph and return its index."""
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    def add_edge(self, edge):
        """This is an undirected graph,
        so we always add edges in both directions."""
        self._edges[edge.from_].append(edge)
        self._edges[edge.to].append(edge.reversed())

    def add_edge_by_indices(self, from_, to):
        """Add an edge using vertex indices."""
        edge = Edge(from_, to)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first, second):
        """Add an edge by looking up vertex indices."""
        from_ = self._vertices.index(first)
        to = self._vertices.index(second)
        self.add_edge_by_indices(from_, to)

    def vertex_at(self, index):
        """Find the vertex by an index."""
        return self._vertices[index]

    def index_of(self, vertex):
        """Find the index of a vertex in the graph."""
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index):
        """Find the vertices that a vertex
        at some index is connected to."""
        return [self.vertex_at(edge.to) for edge in self._edges[index]]

    def neighbors_for_vertex(self, vertex):
        """Look up a vertice's index and find its neighbours"""
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self, index):
        """Look up the index of a vertex and retunr its edges."""
        return self._edges[index]

    def edges_for_vertex(self, vertex):
        """Look up the index of a vertex and retunrs its edges."""
        return self.edges_for_index(self.index_of(vertex))

    def __str__(self):
        """Pretty print a graph."""
        desc = ''
        for i in range(self.vertex_count):
            desc += (f'index: {i} -> {self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n')
        return desc


def get_graph():
    cities = [
        'Seattle', 'San Francisco', 'Los Angeles', 'Riverside', 'Phoenix',
        'Chicago', 'Boston', 'New York', 'Atlanta', 'Miami', 'Dallas',
        'Houston', 'Detroit', 'Philadelphia', 'Washington'
    ]
    graph = Graph(cities)
    graph.add_edge_by_vertices('Seattle', 'Chicago')
    graph.add_edge_by_vertices('Seattle', 'San Francisco')
    graph.add_edge_by_vertices('San Francisco', 'Riverside')
    graph.add_edge_by_vertices('San Francisco', 'Los Angeles')
    graph.add_edge_by_vertices('Los Angeles', 'Riverside')
    graph.add_edge_by_vertices('Los Angeles', 'Phoenix')
    graph.add_edge_by_vertices('Riverside', 'Phoenix')
    graph.add_edge_by_vertices('Riverside', 'Chicago')
    graph.add_edge_by_vertices('Phoenix', 'Dallas')
    graph.add_edge_by_vertices('Phoenix', 'Houston')
    graph.add_edge_by_vertices('Dallas', 'Chicago')
    graph.add_edge_by_vertices('Dallas', 'Atlanta')
    graph.add_edge_by_vertices('Dallas', 'Houston')
    graph.add_edge_by_vertices('Houston', 'Atlanta')
    graph.add_edge_by_vertices('Houston', 'Miami')
    graph.add_edge_by_vertices('Atlanta', 'Chicago')
    graph.add_edge_by_vertices('Atlanta', 'Washington')
    graph.add_edge_by_vertices('Atlanta', 'Miami')
    graph.add_edge_by_vertices('Miami', 'Washington')
    graph.add_edge_by_vertices('Chicago', 'Detroit')
    graph.add_edge_by_vertices('Detroit', 'Boston')
    graph.add_edge_by_vertices('Detroit', 'Washington')
    graph.add_edge_by_vertices('Detroit', 'New York')
    graph.add_edge_by_vertices('Boston', 'New York')
    graph.add_edge_by_vertices('New York', 'Philadelphia')
    graph.add_edge_by_vertices('Philadelphia', 'Washington')
    return graph
