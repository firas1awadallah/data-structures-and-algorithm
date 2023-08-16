from graph_business_trip import Graph, business_trip
graph = Graph()


graph.add_vertex("Amman")
graph.add_vertex("Zarqa")
graph.add_vertex("Irbid")
graph.add_vertex("Jarsh")
graph.add_vertex("Aqaba")
graph.add_vertex("Maan")
graph.add_edge("Zarqa", "Irbid", 82)
graph.add_edge("Irbid", "Jarsh", 150)
graph.add_edge("Jarsh", "Aqaba", 42)
graph.add_edge("Aqaba", "Maan", 73)
graph.add_edge("Maan", "Amman", 250)
graph.add_edge("Maan", "Zarqa", 26)
graph.add_edge("Aqaba", "Zarqa", 105)
graph.add_edge("Jarsh", "Zarqa", 99)
graph.add_edge("Zarqa", "Amman", 37)




def test_case_1():

    city_names = ['Jarsh', 'Aqaba', 'Maan']
    cost = business_trip(graph, city_names)
    assert cost == 115

def test_case_2():

    city_names = ['Maan', 'Irbid']
    cost = business_trip(graph, city_names)
    assert cost is None

def test_case_3():

    city_names = ['Amman', 'Jarsh', 'Maan']
    cost = business_trip(graph, city_names)
    assert cost is None

def test_case_4():
    
    city_names = ["Zarqa", "Irbid"]
    cost = business_trip(graph, city_names)
    assert cost == 82

def test_case_5():
    
    city_names = ["Zarqa"]
    cost = business_trip(graph, city_names)
    assert cost == 0