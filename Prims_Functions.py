from Weighted_Graph import *
G = Weighted_Graph('tested.txt')
G.draw_graph() #Displays Top Graph
V=G.vertex_set()
E=G.edge_set()

############################################################################

def cost(G, e):
    return G.edge_dict()[e]
print('Cost of function at (0,1)')
print('')

############################################################################

def initialize_tree(starting_vertex):
    return ({starting_vertex}, [])
print('The initial tree value is', initial_tree(3)) #Prints initial tree value
print(' ')
T = ({0,1}, [(0,1), (0,2)])     #Assign T values
G.draw_subgraph(T)              #Displays Lower Graph

############################################################################

def incidentEdges(G, T):
    temp_edges = []
    for e in G.edge_set():
        for v in T[0]:
            if v in e:
                edges.append(e)
    return [e for e in temp_edges if e not in T[1]]
print(incident_edges(G, T))
print(' ')

############################################################################   

def valid_incidentEdges(G, T):
    temp_edges = []
    for e in incidentEdges(G, T):
        if e[0] not in T[0] or e[1] not in T[0]:
            temp_edges.append(e)
    return temp_edges
print(valid_incident_edges(G, T))
print(' ')

############################################################################

def findMinEdge(G, T):
    E = valid_incidentEdges(G, T)
    minimum = E[0]
    for e in E:
        if cost(G,e) < cost(G, minimum):
            minimum = e
    return (G, minimum)
print(findMinEdge(G, T))
print(' ')

############################################################################

def update_tree(G, T):
    e = findMinEdge(G,T)
    T[1].append(e)
    T[0].add(e[0])
    T[0].add(e[1])
    
############################################################################
