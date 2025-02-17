class Graph:
    def __init__(self):
        self.adj_list: dict[int, list[int]] = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adj_list:
            self.add_vertex(vertex2)

        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)

    def __str__(self):
        st = []
        for vertex, edges in self.adj_list.items():
            st.append((f"{vertex} -> {edges}"))
        return "\n".join(st)
