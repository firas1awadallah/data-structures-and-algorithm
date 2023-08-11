from graph import Vertix, Edge, Graph
import pytest
@pytest.fixture
def sample_graph():
    g = Graph()
    a = g.add_vertix('A')
    b = g.add_vertix('B')
    e = g.add_vertix('E')
    c = g.add_vertix('C')
    d = g.add_vertix('D')

    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(e, d)
    g.add_edge(e, c)

    return g
# Vertex can be successfully added to the graph
def test_add_vertex(sample_graph):
    v = sample_graph.add_vertix('F')
    assert v in sample_graph.get_vertices()

# An edge can be successfully added to the graph
def test_add_edge(sample_graph):
    f = sample_graph.add_vertix('F')
    g = sample_graph.add_vertix('G')
    sample_graph.add_edge(f, g)
    assert g in [edge.vertix for edge in sample_graph.get_neighbors(f)]

# A collection of all vertices can be properly retrieved from the graph
def test_get_vertices(sample_graph):
    vertices = sample_graph.get_vertices()
    vertex_values = [str(vertex) for vertex in vertices]
    assert len(vertices) == 5
    assert 'A' in vertex_values
    assert 'B' in vertex_values
    assert 'C' in vertex_values
    assert 'D' in vertex_values
    assert 'E' in vertex_values

# The proper size is returned, representing the number of vertices in the graph
def test_size(sample_graph):
    assert sample_graph.size() == 5

# All appropriate neighbors can be retrieved from the graph
def test_get_neighbors(sample_graph):
    a = sample_graph.add_vertix('A')
    b = sample_graph.add_vertix('B')
    sample_graph.add_edge(a, b)  # Add an edge between A and B
    neighbors = sample_graph.get_neighbors(a)
    assert len(neighbors) == 1


def test_breadth_first(sample_graph):
    a = sample_graph.add_vertix('A')
    bft_result = sample_graph.breadth_first(a)
    assert bft_result == ['A']