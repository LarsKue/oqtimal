
from oqtimal.algorithms import sinkhorn_knopp

def optimal_transport(x, y, algorithm="simplex", cost="euclidean", **kwargs):
    return sinkhorn_knopp(x, y, **kwargs)
