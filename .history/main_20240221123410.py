import math
#Hiperparametros del modelo
POPULATION_SIZE = 50
EPOCHS = 10
CHROMOSOME_LENGTH = 5
#value vector example, later we can ask for parameter specification through console
VALUE_VECTOR = [1,2,3,4,5]
# constante para que el operador de cruza solo cambie un bit por default, y se el usuario
# quiere puede cambiar mas
BITS_MUTACION = 1
SURVIVOR_PERCENTAGE=0.1
PORCENTAJE_MUTACION=0.1
PORCENTAJE_REPRODUCCION=1


#checar que solo se creen soluciones validas

def random_init(longitud_cromosoma, tam_poblacion):
    poblacion = list()
    for inviduo in range(tam_poblacion):
        chromosoma = list()
        for gene in range(longitud_cromosoma):
            initializer = 1
            if initializer > 0.5:
                chromosoma.append(1)
            elif initializer <= 0.5:
                chromosoma.append(0)
        poblacion.append(chromosoma)

    return poblacion
  
def fitness_func(cromosoma, value_vector=VALUE_VECTOR):
  valor_total = 0
  for i in range(len(cromosoma)):
    objeto_elegido = cromosoma[i]
    valor_objeto = value_vector[i]
    if objeto_elegido==1:
      valor_total+=valor_objeto

  return valor_total


#recibe el total de la poblacion y te devuelve la fraccion que especifiques como argumento (formato en porcentaje)
def selection_operator(survivor_percentage, poblacion):

  poblacion_con_valores = list()

  for individuo in poblacion:
    poblacion_con_valores.append((individuo, fitness_func(individuo)))

  sorted_individuals = sorted(poblacion_con_valores, key=lambda x: x[1], reverse=True)

  num_sobrevivientes = round(len(poblacion) * survivor_percentage)

  seleccionados = list()

  for i in range(num_sobrevivientes):
    seleccionados.append(sorted_individuals[i])

  return seleccionados


def one_point_crossover(elite, tam_pob):
    if len(elite) % 2 == 0:
        random_point = 0
        middle_point = math.floor(len(elite)/2)

        left_half = elite[:middle_point]
        right_half = elite[middle_point:]

        hijos = list()
        for i in range(middle_point):
            papa = left_half[i]
            mama = right_half[i]
            hijo_1 = papa[:random_point] + mama[random_point:]
            hijo_2 = mama[:random_point] + papa[random_point:]
            hijos.append(hijo_1)
            hijos.append(hijo_2)

        ratio = round(tam_pob / len(hijos))

        new_gen = list()
        for i in range(len(hijos)):
            for _ in range(ratio):
                new_gen.append(hijos[i])
            

        new_gen.append(hijos[0])
        return new_gen
    
    else:
        random_point = 0
        middle_point = math.ceil(len(elite)/2)
        

        left_half = elite[:middle_point]
        right_half = elite[middle_point:]

        hijos = list()
        for i in range(middle_point):
            papa = left_half[i]
            mama = right_half[i]
            hijo_1 = papa[:random_point] + mama[random_point:]
            hijo_2 = mama[:random_point] + papa[random_point:]
            hijos.append(hijo_1)
            hijos.append(hijo_2)

        ratio = round(tam_pob / len(hijos))

        new_gen = list()
        for i in range(len(hijos)):
            for _ in range(ratio):
                new_gen.append(hijos[i])
            

        new_gen.append(hijos[0])
        return new_gen
        

  

def bit_flip_mutation(poblacion,porcentaje_mutacion=PORCENTAJE_MUTACION, bits=BITS_MUTACION):
  """
    Apply bit flip mutation to a chromosome.

    Parameters:
        cromosoma (numpy.ndarray): Binary representation of a chromosome.
        bits (int): Number of bits to mutate.

    Returns:
        numpy.ndarray: Mutated chromosome.
    """
  x_gen = []
  total_mutados = 0
  for cromosoma in poblacion:
    loteria = 44
    if loteria == 50:
      total_mutados+=1
      for _ in range(bits):
        random_bit = 0
        if cromosoma[random_bit] == 0:
          cromosoma[random_bit] = 1
        elif cromosoma[random_bit] == 1:
          cromosoma[random_bit] = 0
    x_gen.append(cromosoma)

  return x_gen, total_mutados

def genetic_algorithm(r_cross=1, r_mut=PORCENTAJE_MUTACION, total_genes=CHROMOSOME_LENGTH, population_size=POPULATION_SIZE,
                      value_vec=VALUE_VECTOR, epochs=EPOCHS, r_selection=SURVIVOR_PERCENTAGE):
  #create initial population
  population = random_init(total_genes,population_size)
  print(len(population))
  #keep track of the best solution
  # for loop for epochs
  for epoch in range(EPOCHS):
    #evaluate all the canidadates in the population
    #score_all = [fitness_func(x) for x in population]
    #selection
    elite = selection_operator(r_selection, population)
    #crossover maintaining the original popualtion size, get parents into pairs
    new_gen = one_point_crossover(elite, population_size)
    #mutation
    x_gen = bit_flip_mutation(new_gen, r_mut)
    #store the new generation
    #replace old population with new population
    population = x_gen

  #when the iterations finish, return the best solution and its score in a tuple
  performance = list()
  for individuo in population:
    performance.append(fitness_func(individuo))
    
  best_score = max(performance)
  index = population.index(best_score)
  best = population[index]
  return best, best_score


best_solution, score = genetic_algorithm()
# print("Done!")
# print('f(%s) = %f' % (best_solution,score))