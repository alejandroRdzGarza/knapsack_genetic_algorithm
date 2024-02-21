

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


def fitness_func(cromosoma, value_vector=VALUE_VECTOR):
    
    
def selection_operator(survivor_percentage, poblacion):
    
    
def one_point_crossover(elite, tam_pob):
    
    
def bit_flip_mutation(poblacion,porcentaje_mutacion=PORCENTAJE_MUTACION, bits=BITS_MUTACION):
    
    
def genetic_algorithm(r_cross=1, r_mut=PORCENTAJE_MUTACION, total_genes=CHROMOSOME_LENGTH, population_size=POPULATION_SIZE,
                      value_vec=VALUE_VECTOR, epochs=EPOCHS, r_selection=SURVIVOR_PERCENTAGE):