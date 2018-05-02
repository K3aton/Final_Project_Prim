from Weighted_Graph import *
from Prims import Prims
#from Kurskals...

def MST(textfile, method = 'Prims', starting_vertex=0, show_cost = False, show=False):
    
    if method == 'Prims':
        return Prims(textfile, starting_vertex, show_cost, show)

    