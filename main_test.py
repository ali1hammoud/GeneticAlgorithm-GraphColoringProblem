import numpy as np
import time

from GA_test import GAlgorthim
from graph import draw_graph

def load_data(path_to_file):
    edges = []
    number_of_vertices = 0
    with open(path_to_file, mode='r') as f:
        for line in f.readlines():
            var, w1, w2 = line.split()[:3]
            if var == 'e':
                edges.append((int(w1)-1, int(w2)-1))
            elif var == 'p':
                number_of_vertices = int(w2)
          
    adjacency_matrix = np.zeros(shape=(number_of_vertices,number_of_vertices),dtype='i')
    for edge in edges:
        if edge[1] > edge[0]:
            adjacency_matrix[edge[0]][edge[1]] = 1
    return adjacency_matrix, number_of_vertices
def optimal_solution(list_first_solution, list_fitness_solution):
    list_fittest_solution = list(zip(list_fitness_solution,list_first_solution))
    sorted_list_fittest_solution = sorted(list_fittest_solution, key=lambda k:k[0])
    solution=list(filter(lambda x: x[0] == sorted_list_fittest_solution[0][0], sorted_list_fittest_solution))
    list_solution=[x[1] for x in solution]
    list_optimal_solution = []
    for x in list_solution:
        if x not in list_optimal_solution:
            list_optimal_solution.append(x)
    return list_optimal_solution
number_of_tries = 1
max_generation = 50
number_of_individuals = 10
number_of_color = 10
mutation_rate = 0.2
mutation_method = '1'
path = 'ali.txt'
adjacency_matrix, number_of_genes = load_data(path)   

list_number_sol_color =[]
list_fitness_solution =[]
list_time =[]
list_first_solution = []

for x in range(number_of_tries):
    start_time = time.time()
    solution_list, fitness_solution, number_sol_color=GAlgorthim( max_generation,number_of_individuals, 
    number_of_genes, number_of_color, mutation_method, mutation_rate, adjacency_matrix)
    
    time_algorthim = "{:.2f}".format(time.time() - start_time)

    print("try number "+str(x+1)+" ==========\n" )
    print("The time of running the algorithm is %s seconds\n" % time_algorthim)
    print('\nThe algorithm found '+str( len(solution_list))+ ' possible solutions\nMinimum number of colors = '+ str(number_sol_color)+
    '\nThe fitness = '+ str(fitness_solution)+'\nNumber of edges = '+str(sum([sum(x) for x in adjacency_matrix]))+'\n')
    print('solution_list',solution_list)
    print('The first possible solution is : ', solution_list[0])
    print('====================================================')
    list_number_sol_color.append(number_sol_color)
    list_fitness_solution.append(fitness_solution)
    list_time.append(time_algorthim)
    list_first_solution.append(solution_list[0])

final_solution = optimal_solution(list_first_solution, list_fitness_solution)
print("\nthe list of the final solution is "+str(final_solution) )
print('the optimal solutions after all tries ',final_solution)  
plot_result(list_number_of_tries, list_max_generation, list_number_of_individuals, list_number_sol_color, list_fitness_solution, list_time)

