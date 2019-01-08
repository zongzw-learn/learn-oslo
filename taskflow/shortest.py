from taskflow import flow
from taskflow import task

edges = {
    'A-B': 3,
    'A-C': 1,
    'A-D': 2,
    'B-E': 2,
    'C-E': 4,
    'C-F': 2,
    'D-F': 4,
    'D-G': 5,
    'E-H': 1,
    'E-I': 3,
    'F-H': 7,
    'G-H': 6,
    'H-I': 8,
    'H-J': 2,
    'I-J': 4
}

distance = {}

path = 'A'

class Finder(task.Task):
    def execute(self, path):
        ps = path.split('-')
        last = ps[-1]

        if not last in distance:
            distance[last] = 0

        result = ''

        for n in edges.keys():
            length = edges[n]

            eps = n.split('-')
            s = eps[0]
            e = eps[1]
            if not e in distance:
                    distance[e] = 0
            if s == last and distance[e] < distance[s] + length:
                distance[e] = distance[s] + length
                result = e
        
        if result == '': return path
        else: return path + '-' + e
                





