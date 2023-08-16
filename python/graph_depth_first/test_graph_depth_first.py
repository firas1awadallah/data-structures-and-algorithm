from graph_depth_first import Graph
g = Graph()

a = g.add_vertex('A')
b = g.add_vertex('B')
c = g.add_vertex('C')
d = g.add_vertex('D')
e = g.add_vertex('E')
f = g.add_vertex('F')
g_vertex = g.add_vertex('G')
h = g.add_vertex('H')

g.add_edge(a, b)
g.add_edge(b, a)

g.add_edge(b, c)
g.add_edge(c, b)

g.add_edge(c, g_vertex)
g.add_edge(g_vertex,c)

g.add_edge(a, d)
g.add_edge(d, a)

g.add_edge(b, d)
g.add_edge(d, b)

g.add_edge(d, e)
g.add_edge(e, d)

g.add_edge(d, h)
g.add_edge(h, d)

g.add_edge(d, f)
g.add_edge(f, d)

def test_depth_first1():

    depth_first=g.depth_first(a)

    assert depth_first == ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']

def test_depth_first2():

    depth_first=g.depth_first(h)

    assert depth_first == ['H', 'D', 'A', 'B', 'C', 'G', 'E', 'F']

def test_depth_first3():

    depth_first=g.depth_first(c)

    assert depth_first == ['C', 'B', 'A', 'D', 'E', 'H', 'F', 'G']





