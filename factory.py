# A simple factory that imports and returns a relevant solver when provided a string
# Not hugely necessary, but reduces the code in solve.py, making it easier to read.

from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ


DefaultMethod = "breadthfirst"
MethodChoices = [
    "astar",
    "breadthfirst",
    "depthfirst",
    "dijkstra",
    "leftturn",
]

DefaultPriorityQueue = "heappq"
PriorityQueueChoices = [
    "heappq",
    "fibheap",
    "fibpq",
    "queuepq"
]

def createsolver(kind, pq_impl=None):
    if kind == "leftturn":
        import leftturn
        return ["Left turn only", leftturn.solve]
    elif kind == "depthfirst":
        import depthfirst
        return ["Depth first search", depthfirst.solve]
    elif kind == "dijkstra":
        import dijkstra
        description = "Dijkstra's Algorithm"
        pq = None
        if pq_impl:
            pq = priority_queue(pq_impl)
            description += " (using %s)" % pq_impl
        else:
            pq = priority_queue(DefaultPriorityQueue)
            description += " (using default %s)" % DefaultPriorityQueue
        return [description, lambda maze: dijkstra.solve(maze, pq)]
    elif kind == "astar":
        import astar
        description = "A-star Search"
        pq = None
        if pq_impl:
            pq = priority_queue(pq_impl)
            description += " (using %s)" % pq_impl
        else:
            pq = priority_queue(DefaultPriorityQueue)
            description += " (using default %s)" % DefaultPriorityQueue
        return [description, lambda maze: astar.solve(maze, pq)]
    else:
        import breadthfirst
        return ["Breadth first search", breadthfirst.solve]

def priority_queue(name):
    if name == "heappq":
        return HeapPQ()
    elif name == "fibheap":
        return FibHeap()
    elif name == "fibpq":
        return FibPQ()
    elif name == "queuepq":
        return QueuePQ()
    else:
        raise ValueError("Unrecognized priorty queue implementation '%s'" % name)
