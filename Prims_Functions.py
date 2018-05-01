
from Weighted_Graph import *
G = Weighted_Graph('tested.txt')
G.draw_graph()
V=G.vertex_set()
E=G.edge_set()



def cost(G, e):
    return G.edge_dict()[e]



def initialize_tree(starting_vertex):
    return ({starting_vertex}, [])



def incidentEdges(G, T):
    temp_edges = []
    for e in G.edge_set():
        for v in T[0]:
            if e not in T[1] and v in e:
                temp_edges.append(e)
    return temp_edges

    

def valid_incidentEdges(G, T):
    temp_edges = []
    for e in incidentEdges(G, T):
        if e[0] not in T[0] or e[1] not in T[0]:
            temp_edges.append(e)
    return temp_edges



def findMinEdge(G, T):
    E = valid_incidentEdges(G, T)
    minimum = E[0]
    for e in E:
        if cost(G,e) < cost(G, minimum):
            minimum = e
    return minimum


def update_tree(G, T):
    e = findMinEdge(G,T)
    T[1].append(e)
    T[0].add(e[0])
    T[0].add(e[1])