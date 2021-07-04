def set_gbest(initial_fitness,Pbest):
    Gbest = Pbest[initial_fitness.index(max(initial_fitness))]
    return Gbest