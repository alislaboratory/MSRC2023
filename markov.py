### WRITTEN BY ALI ASHRAFY 2023
### MATHEMATICS AND STATISTICS RESEARCH COMPETITION
# 13 Aug 2023

### This code is the Markov Chain approach to random walks. Our paper can be found at the GitHub:
# https://github.com/alislaboratory/MSRC2023

import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt


def plot_distribution(n_distribution):
    # Extracting keys and values
    iterations = list(n_distribution.keys())
    probabilities = list(n_distribution.values())
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(iterations, probabilities, color='skyblue')
    plt.xlabel('Nth Iteration')
    plt.ylabel('Probability')
    plt.title('Distribution of Escape Time')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()



def create_grid(n, m):  # create a n rows x m columns grid
    grid = []
    for rows in range(n):
        row = []
        for columns in range(m):
            row.append((columns, rows))

        grid.append(row)

    return grid


# note: we are using 0,0 as top left - can convert later
# note: always make the grid a lot bigger than it needs to be because it is technically an infinite grid.


def create_transition_matrix(
    n, m, grid
):  # Create the initial starting transition matrix
    # initially storing as a 2D dictionary to allow indexing by tuples
    # then convert to numpy for matrixing
    matrix = {}
    temp_array = []
    for a in range(n):
        for b in range(m):
            temp_array.append(grid[a][b])

    for i in range(n * m):
        temp_row = {}
        current_from = temp_array[i]
        x = current_from[0]
        y = current_from[1]
        for j in range(n * m):
            current_to = temp_array[j]
            temp_row[current_to] = 0
            # if it is on the edge... well just make the matrix one bigger than it needs to be limfao
            if current_to in [
                (x, y - 1),
                (x + 1, y),
                (x, y + 1),
                (x - 1, y),
            ]:  # is it immediately surrounding the ting
                temp_row[current_to] = 0.25

        matrix[current_from] = temp_row

    # now convert to matrix
    # pprint(matrix)
    new_matrix = np.zeros(shape=(m * n, m * n))
    for i in range(n * m):
        for j in range(n * m):
            new_matrix[i][j] = matrix[temp_array[i]][temp_array[j]]

    return new_matrix


# create stuffs


def np_to_dict(matrix, grid):  # Unused at the moment
    dicmatrix = {}
    coords = []
    # generate coords
    for i in grid:
        for j in i:
            coords.append(j)

    # generate dictionary
    for i in range(len(coords)):
        temp_row = {}
        for j in range(len(coords)):
            temp_row[coords[j]] = matrix[i][j]

        dicmatrix[coords[i]] = temp_row

    return dicmatrix

gamma = [  # The coordinates for 15a gamma
    (6, 8),
    (7, 8),
    (8, 8),
    (8, 9),
    (9, 9),
    (10, 9),
    (10, 8),
    (10, 7),
    (10, 6),
    (10, 5),
    (9, 5),
    (8, 5),
    (8, 4),
    (8, 3),
    (8, 2),
    (7, 2),
    (6, 2),
    (5, 2),
    (4, 2),
    (4, 3),
    (4, 4),
    (4, 5),
    (3, 5),
    (2, 5),
    (2, 6),
    (2, 7),
    (2, 8),
    (2, 9),
    (3, 9),
    (4, 9),
    (4, 8),
    (5, 8),
]
grid_size = (12,12)
start_pos = (6,6)


# gamma = [ (1, 1), # The minimisation
#     (2, 1),
#     (3, 1),
#     (3, 2),
#     (3, 3),
#     (4, 3),
#     (4, 4),
#     (3, 4),
#     (2, 3),
#     (1, 3),
#     (1, 2),
#     (0, 1),
#     (0, 0),
#     (1, 0)]
# grid_size =(6,6)
# start_pos = (2,2)

# box 6x6
# gamma =[(1,4),(7,4),(7,7),(6,1),(7,2),(7,6),(1,2),(1,7),(1,1),(1,6),(7,5),(7,3),(2,1),(3,1),(4,1),(5,1),(7,1),(6,7),(5,7),(4,7),(3,7),(2,7),(2,1),(1,5),(1,3)] 
# grid_size = (8,8)
# start_pos = (4,4)
# 10.715236686390538

# box with bulge and indentation 6x6
# gamma = [(7,7),(6,1),(7,2),(7,6),(1,2),(1,7),(1,1),(1,6),(7,5),(7,3),(2,1),(3,1),(4,1),(5,1),(7,1),(6,3),(6,4),(6,5),(6,7),(5,7),(4,7),(3,7),(2,7),(0,5),(0,4),(0,3),(2,1),(1,5),(1,3)]
# grid_size = (8,8)
# start_pos = (4,4)
# 8.790242996856136


# gamma = [ (i[0], i[1]+2) for i in gamma] # use this for offsetting
# print(gamma)


grid = create_grid(grid_size[0], grid_size[1])
matrix = create_transition_matrix(grid_size[0], grid_size[1], grid)
n_distribution = {}

summ = 0
n = 1
prev = matrix
last = -1
debug = True
for (
    coord
) in (
    gamma
):  # Set the boundary curve points to be absorbing i.e the spider stays there if it reaches it
    for i in range(len(matrix[coord[0] * len(grid) + coord[1]])):
        matrix[coord[0] * len(grid) + coord[1]][i] = 0

    matrix[coord[0] * len(grid) + coord[1]][coord[0] * len(grid) + coord[1]] = 0

# TESTING #
# m = 1
# while m < 100:
#     prev = np.matmul(prev, matrix)
#     print(prev[6 * len(grid) + 6][0 * len(grid) + 0])

#     m += 1


while True:  # Expected value is sum of n x P(escape time = n) to n = infinity
    currentprob = 0

    for coord in gamma:
        currentprob += prev[start_pos[0] * len(grid) + start_pos[1]][
            coord[0] * len(grid) + coord[1]
        ]  # Find each probability for each gamma coordinate

    summ += n * currentprob  # Add to the expected value sum.
    # Debugging statements
    if debug:
        print(n)
        print(f"Sum: {summ}")
        print(f"Escape prob for {n} steps: {currentprob}")
        print()
    #

    if last == summ and n>grid_size[0]:  # Break when last value = current i.e converged
        print(n)
        print("Yahoo!")  # Yahoo when converged
        break

    last = summ
    n_distribution[n] = currentprob
    prev = np.matmul(prev, matrix)  # Multiply the transition matrices
    n += 1  # Increment n



print(summ)
plot_distribution(n_distribution=n_distribution) # Plot distribution (comment out if not working on Problem D as it will cause trouble)
