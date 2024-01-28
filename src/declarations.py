
import random

''' -------------------------- VALUE CREATION FUNCTIONS HERE -------------------------- '''

def generatePaths(max):
    paths = []
    npath = 1
    while (npath != max):
        path = random.randint(1, (max-1))
        if path not in paths:
            paths.append(path)
            npath += 1
    return paths


''' ----------------------------- CLASS DECLARATIONS HERE ----------------------------- '''

class City:
    def __init__(self, row_name, path, visited):
        self.row_name = row_name
        self.path = path
        self.visited = visited

class Map:
    def __init__(self, size):
        # instead of a literal matrix, we simulate one by creating multiples lists,
        # each list corresponding to a city with their designated paths

        self.graph = []
        nsize = size

        for i in range(0, nsize):
            row = []
            for j in range(0, nsize):
                new_city = City("", 0, 0)
                row.append(new_city)

            self.graph.append(row)
        self.size = nsize

    # prints the map
    def print_map(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                print("[{0}: D={1} V={2}]".format(self.graph[i][j].row_name, self.graph[i][j].path, self.graph[i][j].visited), end=" ")
            print("")
        print("")
