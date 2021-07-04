def fitness(X,particle,particle_amount):
    Fitness = []
    for i in range(particle_amount):
        count_tp = 0
        count_fp = 0
        count_fn = 0
        count_tn = 0
        position = np.array_split(particle[i],2)   
        for j in range(X):
            Class = class_type[j]
            Training_V = training_vector[j,:]
            Dist = np.linalg.norm(Training_V-position[0])
            dist = np.linalg.norm(position[1]-Training_V)
            if(Class == 0):
                if(dist<Dist):
                    count_fp+= 1
                else:
                    count_tn+= 1
            elif(Class == 1):
                if(dist<Dist):
                    count_tp+= 1
                else:
                    count_fn+= 1
        try:
            precision = count_tp/(count_tp+count_fp)
            recall = count_tp/(count_tp+count_fn)
            fitness = (5*precision*recall)/((4*precision)+recall)
        except ZeroDivisionError:
            fitness = 0
        Fitness.append(fitness)
    return Fitness
