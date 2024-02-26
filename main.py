# Este algoritmo genetico intentara encontrar la combinacion
# de eventos en su "vida" que maximizen su "exito"


'''
Representacion:

Chromosoma contara con entre 5-15 (por definir) genes

Cada gene representa un tipo de evento distinto

La representacion a nivel gene sera con numeros reales 
ya que de esta manera tambien puede tomarse en cuenta
cuantas veces repitio un evento en particular.

Cada vez que el individuo decida hacer cierto evento en un dia, se añade uno al slot de ese evento en el cromosoma

Tambien es importante poner requerimientos minimos, por ejemplo se necesitan 1000 dias de estudio para que valga la pena invertir el tiempo.
Esta es la heuristica que vamos a seguir para poder aproximar esta escenario tan complejo.

Entonces un individuo debe de elegir en que vale la pena poner su tiempo, debe de pensar a largo plazo, algunos eventos tienen recompensas a corto
plazo, pero otros eventos son mas tardados pero su recompensa es mayor

Cada individuo contara con 35,000 dias de vida, osea que cada generacion dura 35,000 dias

Categorias de eventos            valor        dias de vida requeridos:

Familia                          10           5000
Dia de trabajo                   2            15000
Dia de estudio                   10           1000
Crear una empresa de exito       100          1800
ETC



Fitness Function:

Operadores Evolutivos:

Seleccion: Se seleccionara al mejor 1% de cada generacion

Cruza: Ver que genes tomar de cada padre para producir el hijo y tambien ver si el tamaño de la poblacion cambia con cada generacion

Mutacion: Ver cual puede ser la mejor manera de mutar aleatoriamente un o varios genes de un cromosoma

Finalmente es importante agregar metricas e inclusive visualizacion para poder ver el estado de nuestra poblacion. Algunas metricas pueden ser:

- Fitness general de cada generacion
- Fitness mas alto dentro de cada generacion
- Fitness mas bajo dentro de cada generacion


'''

import numpy as np

#Hiperparametros del modelo
POPULATION_SIZE = (10, 100, 1000, 1000)
INDIVIDUAL_SIZE = 10
EPOCHS = (10,100,1000,1000)



def random_init(num_genes, tam_poblacion):
    poblacion = list()
    for inviduo in range(tam_poblacion):
        chromosoma = list()
        for gene in range(num_genes):
            initializer = np.random.rand()
            if initializer > 0.5:
                chromosoma.append(1)
            elif initializer <= 0.5:
                chromosoma.append(0)     
        poblacion.append(chromosoma)
        
    return poblacion
    
    
def pop_fitness():
    return 0

        
                
