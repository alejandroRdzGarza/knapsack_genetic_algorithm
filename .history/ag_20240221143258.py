import math
import numpy as np

respuesta = input("escribe 1 si quieres ajustar los parametros, escribe 0 para correr con los valores default")

if int(respuesta) == 1:
    POPULATION_SIZE = input("Tamaño de poblacion")
    EPOCHS = input("Numero de generaciones/iteraciones")
    CHROMOSOME_LENGTH = input("Largo cromosomico")
    #value vector example, later we can ask for parameter specification through console
    VALUE_VECTOR = input("Escribe el vector de valores usando [] y separando los valores con comas")
    # constante para que el operador de cruza solo cambie un bit por default, y se el usuario
    # quiere puede cambiar mas
    BITS_MUTACION = input("Numero de genes a mutar como maximo por individuo")
    SURVIVOR_PERCENTAGE = input("Porcentaje de sobrevivientes, escrito con valores entre 0 y 1")
    PORCENTAJE_MUTACION= input("Porcentaje de individuos mutados, escrito con valores entre 0 y 1")
    PORCENTAJE_REPRODUCCION= input("Porcentaje de reproduccion, con valores entre 0 y 1")
    
else:

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

def random_init(longitud_cromosoma, tam_poblacion):
    poblacion = np.zeros((tam_poblacion, longitud_cromosoma))
    for individuo in range(tam_poblacion):
        chromosome = np.zeros(longitud_cromosoma)
        for gene in range(longitud_cromosoma):
            initializer = np.random.rand()
            if initializer > 0.5:
                chromosome[gene] = 1
        poblacion[individuo] = chromosome
    return poblacion


def fitness_func(cromosoma, value_vector=VALUE_VECTOR):
    return 1
    
    
def selection_operator(survivor_percentage, poblacion):
    scores = np.array(fitness_func(individual) for individual in poblacion)
    
    individuals_with_scores = np.column_stack((poblacion, scores))
    
    sorted_individuals = sorted(individuals_with_scores, key=lambda x: x[-1], reverse=True)
    
    num_sobrevivientes = round(len(poblacion) * survivor_percentage)

    seleccionados = np.array([individual[:-1] for individual in sorted_individuals[:num_sobrevivientes]])

    return seleccionados
    
    
    
# def one_point_crossover(elite, tam_pob):
    
    
# def bit_flip_mutation(poblacion,porcentaje_mutacion=PORCENTAJE_MUTACION, bits=BITS_MUTACION):
    
    
def genetic_algorithm(r_cross=1, r_mut=PORCENTAJE_MUTACION, total_genes=CHROMOSOME_LENGTH, population_size=POPULATION_SIZE,
                      value_vec=VALUE_VECTOR, epochs=EPOCHS, r_selection=SURVIVOR_PERCENTAGE):
    
    population = random_init(total_genes, population_size)
    
    for epoch in range(epochs):
        elite = selection_operator(r_selection, population)
        print(elite)
    
    return 0
    
    
genetic_algorithm()
# best_solution, score = genetic_algorithm()
# print("Done!")
# print('f(%s) = %f' % (best_solution,score))