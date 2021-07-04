def update_particle(particle,new_velocity):
    particle = np.array(particle)
    for i in range(len(particle)):
        particle[i] = particle[i] + new_velocity[i]
        for j,data in enumerate (particle[i]):
            if(particle[i][j] > 1):
                particle[i][j] = 1
            elif(particle[i][j] < 0):
                particle[i][j] = 0
            else: 
                particle[i][j] = particle[i][j]
    return particle