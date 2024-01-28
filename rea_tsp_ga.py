'''
CMSC 170 - Introduction to Artificial Intelligence

Program Description:
    Simulate a Generic Algorithm to solve a Travelling Salesman Problem where we
    find the optimal path based on a given undirected, weighted, adjacency matrix.
    Note that instead of using chromosomes for the genes, distance path was utilized
    to identify the uniqueness of a city in a path.

    The following are the present operations:
        1. Selection
        2. Crossover
        3. Mutation
        4. Fitness Calculator for Paths

Specifications:
    - The initialized graph is an undirected, weighted, adjacency matrix
    - The adjacency is lost within the program due to the operations
    - Longest tested running time was 755 seconds with a 100x100 matrix
    - A constant NUMBER_OF_PATHS can be changed to indicate matrix size
    - Durin running time, the program will keep on printing each generation

@author Ralph Kenneth Rea
@start date: 2023-03-28
@last updated: 2023-05-30

References:
- CMSC 170 Lab Discussion
- https://www.geeksforgeeks.org/python-lists/
- https://www.programiz.com/python-programming/methods/list/
- https://medium.com/@becmjo/genetic-algorithms-and-the-travelling-salesman-problem-d10d1daf96a1

== JUMP TO LINE 235 FOR THE ADJUSTABLE VALUE

'''

import random
import time

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


''' --------------------------- VARIABLE DECLARATIONS HERE --------------------------- '''

CITY_NUMBERS = []
for i in range(0, 100): CITY_NUMBERS.append(str(i))

CITY_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
LEN_NUM = len(CITY_NUMBERS)
LEN_LET = len(CITY_LETTERS)

gen = 0
cities_visited = 0

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


''' -------------------------- PROGRAM FUNCTIONALITIES HERE -------------------------- '''

# returns the fitness level of a destination path
def fitnessLevel(rowcity):

    # fitneess = summation of the distance of each consecutive city
    # where i = city to visit first
    # and i+1 = the next city to visit 

    fitness = 0
    paths = (len(rowcity) - 2)
    for i in range(0, paths):
        fitness = fitness + (rowcity[i].path * i)
    return fitness


# perform selection
def selection(graph, ncities):

    # compile the indeces and determine the role of each
    index_compilation = []
    fittest_value = 0; unfit_value = 0
    fittest_index = 0; unfit_index = 0

    max = ncities
    for i in range(0, max):
        f_val = (fitnessLevel(graph[i]))
        index_compilation.append(i)

        # constantly update the fittest and unfit value
        if i == 0:
            fittest_value = f_val
            unfit_value = f_val
            fittest_index = 0
            unfit_index = 0

        if f_val < fittest_value:
            fittest_index = i
            fittest_value = f_val
        
        if f_val > unfit_value:
            unfit_value = f_val
            unfit_index = i

    index_compilation.remove(fittest_index)     # we will use this array to
    index_compilation.remove(unfit_index)       # select random indeces too

    # perform the roulette selection, where the fittest value has the
    # highest probability, the unift with the lowest, and others

    roulette_probability = random.randint(0, 100)

    if roulette_probability >= 55:
        return fittest_index
    elif roulette_probability >= 0 and roulette_probability < 10:
        return unfit_index
    else:
        other = random.randint(0, (len(index_compilation)-1))
        return other


# perform crossover here
def crossover(rowcity1, rowcity2, ncities):

    # for the crossover operation, the Partially Matched Crossover (PMX) was implemented,
    # wherein we replace specific crossover sites from a city to another, we pass over
    # the original cities to the other one, creating a somewhat new offspring 
    
    length = (ncities // 2)-1
    if length <= 0: return rowcity1
    else:
        start = length
        end = (length + 2)

        # collect the cities that will be used for crossover
        swap1, swap2 = [], []
        for i in range(start, end):
            swap1.append(rowcity1[i])
            swap2.append(rowcity2[i]) 

        to_swap = start                     # index of current site of crossover
        swap_time = (len(swap1) - 1)        # iterations for swapping

        for i in range(0, swap_time):

            # first look for the instance of the path in the row
            replace1 = replace2 = 0
            for o in range(0, ncities):
                if rowcity1[o].path == swap2[i].path:
                    replace1 = o
            for p in range(0, ncities):
                if rowcity2[o].path == swap1[i].path:
                    replace2 = p

            # swap cities for path 1 here
            temp1 = rowcity1[to_swap]
            rowcity1[to_swap] = swap2[i]
            rowcity1[replace1] = temp1

            # swap cities for path 2 here
            temp2 = rowcity2[to_swap]
            rowcity2[to_swap] = swap1[i]
            rowcity2[replace2] = temp2


# perform mutation where we swap two sites in a row city
def mutation(mutatecity, ncities):

    # here, we initialized a swapping method since we do not want to
    # change the visited status of the cities, we take the index of
    # the cities to swap instead of reinitializing the cities

    max = (ncities - 1)
    index1 = random.randint(0, max)
    while True:
        index2 = random.randint(0, max)
        if index2 != index1:
            break
    # swapping of cities here
    temp = mutatecity[index1]
    mutatecity[index1] = mutatecity[index2]
    mutatecity[index2] = temp
    return mutatecity
    

''' ------------------------------- START OF PROGRAM ------------------------------- '''

start = time.time()

''' IMPORTANT: 
    The NUMBER_OF_PATHS constant here determines the supposed matrix size to be used.
    The number of paths is also equal to the number of possible row / col elements.
    For a 10x10 matrix, the input value will be 10.

    For the recent run of a 100 x 100 matrix, the code ran for 755 seconds.
''' 

NUMBER_OF_PATHS = 100

''' ------------------------------------------------------------------------------- '''

first_country = Map(NUMBER_OF_PATHS)
country = Map(NUMBER_OF_PATHS)

msize = country.size

# initialize the names such that a row has same names
lcount = 0; ncount = 0
path_names = []
for i in range(0, msize):
    city_name = "" + CITY_LETTERS[lcount] + CITY_NUMBERS[ncount]

    lcount += 1
    if lcount >= LEN_LET: lcount = 0; ncount += 1
    if ncount >= LEN_NUM: ncount = 0
    path_names.append(city_name)

for k in range(0, msize):
    for l in range(0, msize):
        country.graph[k][l].row_name = path_names[k]
        first_country.graph[k][l].row_name = path_names[k]


# generate random city paths for the map matrix
new_paths = generatePaths(msize)
print(new_paths)

for i in range(0, msize-1):
    for j in range(i, msize):

        # this condition makes sure that the matrix contains adjacency property
        if i != j:

            # make sure that the value doesn't repeat in a row / column
            for k in range(0, msize):
                if new_paths[0] == country.graph[i][k].path:
                    new_paths.append(new_paths.pop(0))
                    break
            for l in range(0, msize):
                if new_paths[0] == country.graph[j][l].path:
                    new_paths.append(new_paths.pop(0))
                    break

            # append the new, unique distance path of the city
            first_country.graph[i][j].path = new_paths[0]
            first_country.graph[j][i].path = new_paths[0]
            
            country.graph[i][j].path = new_paths[0]
            country.graph[j][i].path = new_paths[0]
            new_paths.append(new_paths.pop(0))
            # place the popped path to the end of list to open new paths


''' --------- AFTER GENERATING THE CITY, PERFORM THE GENETIC ALGORITHM HERE --------- '''

print("\nGeneration 1")
country.print_map()
gen += 1
# fitnessLevel(country)

while True:

    for i in range(0, msize):
        for j in range(0, msize):

            # check first if a city is visited or not
            if country.graph[i][j].visited == 0:
                country.graph[i][j].visited = 1
                country.graph[j][i].visited = 1

                # update counters
                cities_visited += 1
                gen += 1

                # perform selection / crossover here
                while True:
                    parent1 = selection(country.graph, msize)
                    parent2 = selection(country.graph, msize)
                    if parent1 != parent2: break
                crossover(country.graph[parent1], country.graph[parent2], msize)

                # may perform probable mutation of a random city
                mutation_probability = random.randint(0, 100)
                if mutation_probability <= 10:
                    paths = random.randint(0, (msize-1))
                    mutated_paths = mutation(country.graph[paths], msize)

                    # reinitialize the new paths of the selected random city path list
                    country.graph[paths] = mutated_paths
                    print("== Mutation occured at site: {0} ".format(country.graph[paths][0].row_name))

                print("Generation {0}: ".format(gen))
                country.print_map()

    # after each end of for loop iteration, check if all values were visited
    invalid = 0
    for i in range(0, msize):
        if invalid == 1: break
        for j in range(0, msize):
            if country.graph[i][j].visited == 0:
                invalid = 1
                break
    # end loop here if all visited
    if invalid == 0: break

print("-- end of loop \n\n")


''' --------------------------------- END OF LOOP HERE --------------------------------- '''

# print the fitness value of each path
fittest_value = 0
fittest_index = 0
for i in range(0, msize):
    path_fitness = fitnessLevel(country.graph[i])

    # with the changes in the row names due to the multiple instances of mutation and crossover,
    # we then print the names in the first initialized path_names list since it has the unedited names
    # technically, first row will always be row A0 despite the shfits in cities and more

    print("Fitness Value of Row ({0}) {1}: {2}".format((i+1), path_names[i], path_fitness))
    if i == 0:
        fittest_value = path_fitness
        fittest_index = 0
    if path_fitness < fittest_value:
        fittest_value = path_fitness
        fittest_index = i


# print the computed optimal path and distances

print("\nBest path plan: {0} (Fitness: {1})".format(path_names[fittest_index], fittest_value))
print("Distance of each city: ", end ="")
for j in range(0, msize):
    print("{0} ".format(country.graph[fittest_index][j].path), end=" ")
print("\n")


# indicate the end of the program
end = time.time()
print("Ended at Generation {} ".format(gen))
print("Time elapsed: {0} seconds\n".format(round((end - start), 2)))
