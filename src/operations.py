
import random

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
