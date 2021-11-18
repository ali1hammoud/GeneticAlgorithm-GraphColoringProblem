from GA import GAlgorthim
from graph import draw_graph
from readdata import load_data
import time
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#create a new window and assign it to the variable 'root'
root= Tk()
#set the title of the window
root.title("GCP")
#set the icon of the window
#root.iconbitmap("Img/kubsu.ico")
#set the dimensions of the window
root.geometry("1100x600")
#fixed size of window
root.resizable(0, 0)
#number_of_tries
lbl_number_of_tries = Label(root, text='Number of tries : ')
lbl_number_of_tries.grid( row=0, column=0, padx=5, pady=5)
ent_number_of_tries = Entry(root, width=35, borderwidth=5)
ent_number_of_tries.insert(END, '1')
ent_number_of_tries.grid(row=0, column=1, padx=5, pady=5)
#number_of_individuals
lbl_number_of_individuals = Label(root, text='Number of individuals : ')
lbl_number_of_individuals.grid( row=1, column=0, padx=5, pady=5)
ent_number_of_individuals = Entry(root, width=35, borderwidth=5)
ent_number_of_individuals.insert(END, '100')
ent_number_of_individuals.grid(row=1, column=1, padx=5, pady=5)
#increase_of_individuals
lbl_increase_of_individuals = Label(root, text='The increase of individuals in every new try : ')
lbl_increase_of_individuals.grid( row=2, column=0, padx=5, pady=5)
ent_increase_of_individuals = Entry(root, width=35, borderwidth=5)
ent_increase_of_individuals.insert(END, '0')
ent_increase_of_individuals.grid(row=2, column=1, padx=5, pady=5)
#max_generation
lbl_max_generation = Label(root, text='The max generation : ')
lbl_max_generation.grid( row=3, column=0, padx=5, pady=5)
ent_max_generation = Entry(root, width=35, borderwidth=5)
ent_max_generation.insert(END, '100')
ent_max_generation.grid(row=3, column=1, padx=5, pady=5)
#increase_of_max_generation
lbl_increase_of_max_generation = Label(root, text='The increase of max generation in every new try : ')
lbl_increase_of_max_generation.grid( row=4, column=0, padx=5, pady=5)
ent_increase_of_max_generation = Entry(root, width=35, borderwidth=5)
ent_increase_of_max_generation.insert(END, '0')
ent_increase_of_max_generation.grid(row=4, column=1, padx=5, pady=5)
#number_of_genes
lbl_number_of_genes = Label(root, text='The number of vertics : ')
lbl_number_of_genes.grid( row=5, column=0, padx=5, pady=5)
ent_number_of_genes = Entry(root, width=35, borderwidth=5)
ent_number_of_genes.insert(END, '8')
ent_number_of_genes.grid(row=5, column=1, padx=5, pady=5)
#number_of_color
lbl_number_of_color = Label(root, text='The number of colors : ')
lbl_number_of_color.grid( row=6, column=0, padx=5, pady=5)
ent_number_of_color = Entry(root, width=35, borderwidth=5)
ent_number_of_color.insert(END, '3')
ent_number_of_color.grid(row=6, column=1, padx=5, pady=5)
#mutation_rate
lbl_mutation_rate = Label(root, text='The mutation rate : ')
lbl_mutation_rate.grid( row=7, column=0, padx=5, pady=5)
ent_mutation_rate = Entry(root, width=35, borderwidth=5)
ent_mutation_rate.insert(END, '0.2')
ent_mutation_rate.grid(row=7, column=1, padx=5, pady=5)
#method_algorthim
lbl_method_algorthim = Label(root, text='The method algorthim : ')
lbl_method_algorthim.grid( row=8, column=0, padx=5, pady=5)
combo_method_algorthim = ttk.Combobox(root, values=["custom","random"], state="readonly")
combo_method_algorthim.current(0)
combo_method_algorthim.grid(row=8, column=1)
#select a file
path='ali.txt'
def select_file():
    global path
    path = filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("txt files","*.txt"),("all files","*.*")))
btn_select_file = Button(root, text='select a graph', command=select_file)
btn_select_file.grid(row=8, column=2, padx=5, pady=5)
#population_method
lbl_population_method = Label(root, text='The population method : ')
lbl_population_method.grid( row=9, column=0, padx=5, pady=5, sticky=W)
radio_population_method = StringVar()
rdioOne_population_method = Radiobutton(root, text='first method',
                             variable=radio_population_method, value='1') 
rdioTwo_population_method = Radiobutton(root, text='second method',
                             variable=radio_population_method, value='2') 
rdioThree_population_method = Radiobutton(root, text='third method',
                             variable=radio_population_method, value='3')
rdioOne_population_method.grid(column=0, row=10, sticky=W)
rdioTwo_population_method.grid(column=0, row=11, sticky=W)
rdioThree_population_method.grid(column=0, row=12, sticky=W)
#fitness_method
lbl_fitness_method = Label(root, text='The fitness method : ')
lbl_fitness_method.grid( row=9, column=1, padx=5, pady=5, sticky=W)
radio_fitness_method = StringVar()
rdioOne_fitness_method = Radiobutton(root, text='number of fault',
                             variable=radio_fitness_method, value='1') 
rdioTwo_fitness_method = Radiobutton(root, text='number of fault and color',
                             variable=radio_fitness_method, value='2') 
rdioOne_fitness_method.grid(column=1, row=10, sticky=W)
rdioTwo_fitness_method.grid(column=1, row=11, sticky=W)
#crossover_method
lbl_crossover_method = Label(root, text='The crossover method : ')
lbl_crossover_method.grid( row=9, column=2, padx=5, pady=5, sticky=W)
radio_crossover_method = StringVar()
rdioOne_crossover_method = Radiobutton(root, text='Single point',
                             variable=radio_crossover_method, value='SPC') 
rdioTwo_crossover_method = Radiobutton(root, text='Four point',
                             variable=radio_crossover_method, value='FPC') 
rdioOne_crossover_method.grid(column=2, row=10, sticky=W)
rdioTwo_crossover_method.grid(column=2, row=11, sticky=W)
#mutation_method
lbl_mutation_method = Label(root, text='The mutation method : ')
lbl_mutation_method.grid( row=13, column=0, padx=5, pady=5, sticky=W)
radio_mutation_method = StringVar()
rdioOne_mutation_method = Radiobutton(root, text='change places',
                             variable=radio_mutation_method, value='1') 
rdioTwo_mutation_method = Radiobutton(root, text='change colors',
                             variable=radio_mutation_method, value='2') 
rdioOne_mutation_method.grid(column=0, row=14, sticky=W)
rdioTwo_mutation_method.grid(column=0, row=15, sticky=W)
text = Text(root, width=50, bd = 5, )
text.grid(column=3, row=0, rowspan=13, padx=1, pady=1)
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

def plot_result(list_number_of_tries, list_max_generation, list_number_of_individuals, list_number_sol_color, list_fitness_solution, list_time):
    from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.figure import Figure
    
    # Toplevel object which will  
    # be treated as a new window 
    result_window = Toplevel(root)  
    # sets the title of the 
    # Toplevel widget 
    result_window.title("Results") 
    # sets the geometry of toplevel 
    result_window.geometry("500x500") 
    # A Label widget to show in toplevel 
    Label(result_window, text ="This is the result").pack()
    fig = Figure(figsize=(5, 4), dpi=100)
    fig.subplots_adjust(hspace=0.5)
    ax1=fig.add_subplot(211)
    ax2=fig.add_subplot(212)
    ax1.set_xlabel('max_generation')
    ax1.set_ylabel('time')
    ax2.set_xlabel('population')
    ax2.set_ylabel('fitness')
    ax1.scatter(list_max_generation, list_time)
    ax2.scatter(list_number_of_individuals, list_fitness_solution)
    canvas = FigureCanvasTkAgg(fig, master=result_window)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, result_window)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
def start():
    number_of_tries = int(ent_number_of_tries.get())
    number_of_individuals = int(ent_number_of_individuals.get())
    increase_of_individuals = int(ent_increase_of_individuals.get())
    max_generation = int(ent_max_generation.get())
    increase_of_max_generation = int(ent_increase_of_max_generation.get()) 
    number_of_genes = int(ent_number_of_genes.get())
    number_of_color = int(ent_number_of_color.get())
    mutation_rate = float(ent_mutation_rate.get())
    method_algorthim= combo_method_algorthim.get()
    population_method = radio_population_method.get()
    fitness_method = radio_fitness_method.get()
    crossover_method = radio_crossover_method.get()
    mutation_method = radio_mutation_method.get()
    if method_algorthim == 'random':
        #Random adjacency matrix
        adjacency_matrix = [[random.randint(0, 1) for x in range(number_of_genes)] for y in range(number_of_genes)]
        for i in range(number_of_genes):
            for j in range(number_of_genes):
                if j <= i and adjacency_matrix[j][i] == 1:
                    adjacency_matrix[j][i] = 0
    elif method_algorthim == 'custom':
        adjacency_matrix = load_data(path, number_of_genes)
    ## We can choose two method random to create a random edges between nodes or custom to define our edges in adjacency matrix form
    ## in the random method the fourth parameter returned by GAlgorthim will by the adjacency matrix which created randomly
    with open('Result.txt', 'w') as result:
        result.write('max_generation,populition,number_of_solutions,number_of_color,fitness,time\n')
        list_number_of_tries = [x for x in range(1,number_of_tries+1)]
        list_max_generation=[]
        list_number_of_individuals=[]
        list_number_sol_color=[]
        list_fitness_solution=[]
        list_time=[]
        list_first_solution=[]
        
        for x in range(number_of_tries):
            start_time = time.time()
            solution_list, fitness_solution, number_sol_color=GAlgorthim(population_method, fitness_method, crossover_method,mutation_method,
                                                        number_of_individuals, max_generation, number_of_genes, number_of_color, mutation_rate, adjacency_matrix)
                     
            time_algorthim = "{:.2f}".format(time.time() - start_time)
            
            text.insert(END, "try number "+str(x+1)+" ==========\n" )
            text.insert(END, "The time of running the algorithm is %s seconds\n" % time_algorthim)
            text.insert(END, "The populition = " + str(number_of_individuals))
            text.insert(END, "\nThe max genertion = " + str(max_generation))
            text.insert(END, '\nThe algorithm found '+str( len(solution_list))+ ' possible solutions\nMinimum number of colors = '+ str(number_sol_color)+
                  '\nThe fitness = '+ str(fitness_solution)+'\nNumber of edges = '+str(sum([sum(x) for x in adjacency_matrix]))+'\n')
            print("The time of running the algorithm is %s seconds " % time_algorthim)
            print('solution_list',solution_list)
            print("The populition is = " , number_of_individuals)
            print('The algorithm found ', len(solution_list), 'possible solutions\nMinimum number of colors = ', number_sol_color,
                  '\nThe fitness = ', fitness_solution,'\nNumber of edges = ',sum([sum(x) for x in adjacency_matrix]))
            print('solution_list',solution_list)
            print('The first possible solution is : ', solution_list[0])
            print('====================================================')
            result.write(str(max_generation)+','+str(number_of_individuals)+','+ str(len(solution_list))+','+ str(number_sol_color)+','+
                         str(fitness_solution)+','+ str(time_algorthim)+'\n')      

            list_max_generation.append(max_generation)
            list_number_of_individuals.append(number_of_individuals)
            list_number_sol_color.append(number_sol_color)
            list_fitness_solution.append(fitness_solution)
            list_time.append(time_algorthim)
            list_first_solution.append(solution_list[0])

            number_of_individuals += increase_of_individuals
            max_generation += increase_of_max_generation
    final_solution = optimal_solution(list_first_solution, list_fitness_solution)
    text.insert(END, "\nthe list of the final solution is "+str(final_solution) )
    print('the optimal solutions after all tries ',final_solution)      
    plot_result(list_number_of_tries, list_max_generation, list_number_of_individuals, list_number_sol_color, list_fitness_solution, list_time)
    #Drawing the graph

    global idx_solution
    global number_of_solution
    idx_solution = 0
    number_of_solution = len(final_solution)
    def next_solution(number_of_genes, adjacency_matrix, number_of_color, show_solution):
        global idx_solution
        global number_of_solution
        idx_solution += 1
        if idx_solution == number_of_solution:
            Button_solution = Button(root, text="Quit ...", width= 15, command=root.destroy)
            Button_solution.grid(row=13, column=2, padx=5, pady=5)
        else:
            Button_solution = Button(root, text="next solution", width= 15, command=lambda: next_solution(number_of_genes, adjacency_matrix, number_of_color, final_solution[idx_solution]))
            Button_solution.grid(row=13, column=2, padx=5, pady=5)
        draw_graph(number_of_genes, adjacency_matrix, number_of_color, show_solution)

    Button_solution = Button(root, text="display solution", width= 15, command=lambda: next_solution(number_of_genes, adjacency_matrix, number_of_color, final_solution[idx_solution]))
    Button_solution.grid(row=13, column=2, padx=5, pady=5)

Button_strat = Button(root, text="Start", width= 15, command=start)
Button_strat.grid(row=13, column=1, padx=5, pady=5)
#window.mainloop() tells Python to run the Tkinter event loop. 
#This method listens for events, such as button clicks or keypresses
#and blocks any code that comes after it from running until the window it’s called on is closed. 
root.mainloop()
