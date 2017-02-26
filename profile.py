#!/usr/bin/env python

from bprofile import BProfile

import tempfile
import time
from solve import solve
import factory

inputs = [
    "tiny",
    "small",
    "normal",
    "braid200",
    "logo",
    "combo400",
    "braid2k",
    "perfect2k",
    # "perfect4k",
    # "combo6k",
    # "perfect10k",
    # "vertical15k",
]

def profile_solver(method, priority_queue=None):
    name = method
    if priority_queue:
        name += "-" + priority_queue
    with BProfile("%s.png" % name) as profiler:
        for i in inputs:
            with tempfile.NamedTemporaryFile(suffix=".png") as tmp:
                solve("examples/%s.png" % i, tmp.name, method, priority_queue)

def uses_priority_queue(method):
    return method in ["astar", "dijkstra"]

def main():
    for m in factory.MethodChoices:
        method_start = time.time()
        if uses_priority_queue(m):
            for pq in factory.PriorityQueueChoices:
                profile_solver(m, pq)
        else:
            profile_solver(m)
        method_end = time.time()
        print "*** Elapsed time for %s: %d" % (m, method_end - method_start)

if __name__ == "__main__":
    main()
