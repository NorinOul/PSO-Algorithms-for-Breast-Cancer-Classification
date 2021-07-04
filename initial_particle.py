def initial_particle(particle_amount, dataset_attribute):
    position = []
    for i in range (particle_amount):
        position_element = []
        for j in range (dataset_attribute):
            position_element.append(random.uniform(0,1))
        position.append(position_element)
    return position