
from Prims_Functions import *
from Weighted_Graph import *



def Prims(textfile, starting_vertex = 0, show_cost = False, show = False):
    
    G = Weighted_Graph(textfile)    
    T = initialize_tree(starting_vertex)
    
    while T[0] != G.vertex_set():
        update_tree(G, T)
        
    if show == True:
        G.draw_subgraph(T)
        
    if show_cost == True:
        c = 0
        for e in T[1]:
            c += cost(G, e)
        print('Optimal tree cost:', c)
        
    return T
