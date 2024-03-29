import random

#Generate random individuals for population 
def individual(number_of_genes, number_of_color):
    individual = []
    for i in range(number_of_genes):
        individual.append(random.randint(0, number_of_color-1))
    return individual
#Generate random population method number 1 
def population(number_of_individuals,number_of_genes, number_of_color):
    return [individual(number_of_genes, number_of_color) 
        for x in range(number_of_individuals)]

#Fitness Function method number 1 'fault'
def fitness_calculation(individual, adjacency_matrix):
    fitness_fault = 0
    for i in range(len(individual)-1):
        for j in range(len(individual)):
            if individual[i] == individual[j] and adjacency_matrix[j][i] == 1:
                fitness_fault += 1
    fitness_value =  fitness_fault
    return fitness_value

def fittest(solution_list):
    fittest_value_list = []
    for fittest_solution in solution_list:
        my_dict = {i:fittest_solution.count(i) for i in fittest_solution}
        fittest_value = len(my_dict)
        fittest_value_list.append(fittest_value)
    fittest_list = list(zip(fittest_value_list,solution_list))
    sorted_fittest_list = sorted(fittest_list, key=lambda k:k[0])
    solution=list(filter(lambda x: x[0] == sorted_fittest_list[0][0], sorted_fittest_list))
    number_colors_solution = solution[0][0]
    solution=[x[1] for x in solution]
    return number_colors_solution, solution

def selection(sorted_population):
    num = len(sorted_population)
    n = round(num / 4)
    k = num - n
    # Elitism Selection
    elite_genertion = sorted_population[0: n]
    # Random Selection
    random_genertion = random.choices(sorted_population, k=k)
    selected_genertion = elite_genertion + random_genertion
    return selected_genertion

def crossover_point(number_of_genes):
    p1 = random.randint(0,round(number_of_genes/4))
    p2 = random.randint(round(number_of_genes/4),round(number_of_genes/2))
    p3 = random.randint(round(number_of_genes/2),round(number_of_genes*3/4))
    p4 = random.randint(round(number_of_genes*3/4),number_of_genes-1)
    point_list= [p1,p2,p3,p4]
    return point_list
def crossover_1(parent_list):
    for x in range(0,len(parent_list),2):
        #Generate random four point for every parent to make offspring between them
        point_list = crossover_point(len(parent_list[0]))
        parent_list[x][point_list[0]:point_list[1]],parent_list[x+1][point_list[0]:point_list[1]] = parent_list[x+1][point_list[0]:point_list[1]], parent_list[x][point_list[0]:point_list[1]] 
        parent_list[x][point_list[2]:point_list[3]],parent_list[x+1][point_list[2]:point_list[3]] = parent_list[x+1][point_list[2]:point_list[3]], parent_list[x][point_list[2]:point_list[3]]   
    return parent_list

def mutation_individual_1(individual):
    idx = range(len(individual))
    i1, i2 = random.sample(idx, 2)
    individual[i1], individual[i2] = individual[i2], individual[i1]
    return individual
def mutation_individual_2(individual,adjacency_matrix,number_of_color):
    for i in range(len(individual)-1):
        for j in range(len(individual)):
            if individual[i] == individual[j] and adjacency_matrix[j][i] == 1:
                while True:
                    new_color = random.randint(0, number_of_color-1)
                    if individual[i] != new_color:
                        individual[i] = new_color
                        break
    return individual
#mutation_rate < 1
def mutation(mutation_method, adjacency_matrix, number_of_color, child_list, mutation_rate):
    num = round(len(child_list)*mutation_rate)
    idx_list =  range(len(child_list))
    idx_individuals =  random.sample(idx_list, num)
    for x in idx_individuals:
        if mutation_method == '1':
            mutation_individual_1(child_list[x])
        else:
            mutation_individual_2(child_list[x],adjacency_matrix,number_of_color)
    return child_list
    
    solution_list, fitness_solution, number_sol_color=GAlgorthim( max_generation,number_of_individuals, 
    number_of_genes, number_of_color, mutation_method, mutation_rate, adjacency_matrix)
def GAlgorthim(max_generation,number_of_individuals, 
    number_of_genes, number_of_color, mutation_method, mutation_rate, adjacency_matrix):
      
    #Generate population
    generation=population(number_of_individuals, number_of_genes, number_of_color)
    
    num_generation = 1
    optimal_fitness = 999999999
    optimal_sol_list = []

    while( num_generation <= max_generation):
        # 1- calculate the fitness for every individual in the population
        fitness = []
        for individual in generation:
            fitness.append(fitness_calculation(individual, adjacency_matrix))
            
        individual_fitness_list = list(zip(fitness, generation))
        sorted_individual = sorted(individual_fitness_list, key=lambda k: k[0])
        optimal_sorted_individual = list(filter(lambda x: x[0] == sorted_individual[0][0], sorted_individual))
        
        #Add the best individual to the optimal solution list
        if (optimal_sorted_individual[0][0] == 0):
            #print('found the solution in genertion number ', num_generation)
            optimal_fitness = optimal_sorted_individual[0][0]
            for x in optimal_sorted_individual:
                optimal_sol_list.append([optimal_fitness,list(x[1])])

        elif (optimal_sorted_individual[0][0] < optimal_fitness):
            optimal_fitness = optimal_sorted_individual[0][0]
            optimal_sol = list(optimal_sorted_individual[0][1])
            optimal_sol_list.append([optimal_fitness,optimal_sol])


        sorted_individual = [x[1] for x in sorted_individual]
        # 2- Selecte the parents
        parents = selection(sorted_individual)
        # 3- Crossover operation
        children = crossover_1(parents)
        
        if optimal_sorted_individual[0][0] == 0:
            optimal_sorted_individual = [x[1] for x in optimal_sorted_individual]
            new_number_of_color,e = fittest(optimal_sorted_individual)
            if new_number_of_color < number_of_color:
                number_of_color = new_number_of_color
                    #print('Start again with number of color = ', number_of_color)
                
                generation=population(number_of_individuals, number_of_genes, number_of_color)
                num_generation = 1
            else:
                generation= mutation(mutation_method, adjacency_matrix, number_of_color, children, mutation_rate)
                num_generation += 1             
        else:
            if optimal_sorted_individual[0][0] == number_of_color:
                optimal_sorted_individual = [x[1] for x in optimal_sorted_individual]
                new_number_of_color,e = fittest(optimal_sorted_individual)
                if new_number_of_color < number_of_color:
                    number_of_color = new_number_of_color
                    print('Start again with number of color = ', number_of_color)
                    generation=population(number_of_individuals, number_of_genes, number_of_color)
                    num_generation = 1
                else:
                    generation= mutation(mutation_method, adjacency_matrix, number_of_color, children, mutation_rate)
                    num_generation += 1       
            else:
                generation= mutation(mutation_method, adjacency_matrix, number_of_color, children, mutation_rate)
                num_generation += 1 

    optimal_sol_list=sorted(optimal_sol_list, key=lambda k: k[0])
    optimal_sol_list=list(filter(lambda x: x[0] == optimal_sol_list[0][0], optimal_sol_list))
    optimal_sol_list=[x[1] for x in optimal_sol_list]
    number_sol_color,ss=fittest(optimal_sol_list)
    s = []
    for x in ss:
        if x not in s:
            s.append(x)

    fitness_s = fitness_calculation(s[0], adjacency_matrix)
    return s,fitness_s,number_sol_color


