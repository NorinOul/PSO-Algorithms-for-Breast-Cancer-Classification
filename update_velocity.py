def update_velocity(Pbest,Gbest,velocity,particle):
    rand1 = random.uniform(0,1)
    rand2 = random.uniform(0,1)
    c1 = 0.2
    c2 = 0.2
    Pbest = np.array(Pbest)
    velocity = np.array(velocity)
    Gbest = np.array(Gbest)
    for i in range(len(velocity)):
        velocity[i] = velocity[i] + [c1 * rand1 * (Pbest[i] - particle[i])] + [c2 * rand2 * (Gbest - particle[i])]
    return velocity