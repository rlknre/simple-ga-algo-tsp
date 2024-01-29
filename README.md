
# TSP (GENETIC ALGORITHM)

![Python][py-md-badge]

A **_terminal-based_** simulator of a **_travelling salesman problem_** that uses a simple Genetic Algorithm for solving. It finds the optimal path using data from an undirected, weighted, adjacency matrix that is generated based on the number of paths the user inputs.
- ``main.py`` contains the code for the simple Genetic Algorithm (GA)
- GA operations are found in ``operations.py``
- Class definitions are located in ``declarations.py``
<br />

## Table of Contents
1. [Requirements](#requirements)
2. [How to Run](#instructions)
3. [Functionalities](#functions)
4. [Other Notes](#note)
<br />

## Requirements <a name="requirements"></a>
1. Ensure that the system has Python.
    - To check if you have Python installed, type in any terminal:
      - `python`
    - For installation, you may download it in any application store or through the Python website.
      - https://www.python.org/downloads/

2. When downloading the files, make sure that this directory tree is followed:

   ```
    simple-ga-algo-tsp
    ├── main.py
    ├── src
    │   ├── __pycache__
    │   ├── __init__.py
    │   ├── declarations.py
    │   └── operations.py
    └── README.md
   ```
<br />

## Running Project <a name="instructions"></a>
1. Check the ``main.py`` file and search for the variable **NUMBER_OF_PATHS**.
    - It should be found at _Line 79_.
    - Adjust the value according to your liking:
   
      ```
      Minimum value tested: 4
      Maximum value tested: 100
      ```
      
3. To run the program, proceed to the directory where ``main.py`` is found. In the terminal, run ``python main.py``.

4. Wait for the program to end its run. It will continuously print the matrix for each generation.

5. At the end of the run, it will display the following outputs:
    - Fitness level of each path (row).
    - The Row name of the best path.
    - Distance of each city of the best path.
    - Generation number when all cities are visited.
    - Time elapsed.
<br />

## Functionalities <a name="functions"></a>
Here is a basic rundown of what happens during runtime:
1. Based on the value of **NUMBER_OF_PATHS**, an undirected, weighted, adjacency matrix in the form of a **Map** class will be generated containing **City** classes.
  
2. Randomly generated paths will be created. Each row of the matrix will contain cities with the following values:
   - **City / Row Name**: Generated in main.py
   - **Path**: The distance to this city, it has a unique gene / value.
   - **Visited**: Tells whether the city is visited or not.

3. A while loop runs, ensuring that it visits all the cities each row to search for the optimal path.
 
4. During the loop, each visited city follows the following process repeatedly:
   - **Selection**: Selects two cities based on its fitness level. Mutation of path distance may occur.
   - **Crossover**: Create a new offspring based on the paths of the selected parent cities.
   - **Mutation**: Randomly swap two cities in a path.

5. After visiting all paths, the fitness level is computed to determine the optimal path.

<br />

##
### Author
- Ralph Kenneth Rea

##
### Note <a name="note"></a>
- This is a lab exercise in fulfillment of the requirements in CMSC 170: Introduction to Artificial Intelligence. UPLB.

[py-md-badge]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
