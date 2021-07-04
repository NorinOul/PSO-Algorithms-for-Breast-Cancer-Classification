def initial_velocity(particle_amount, dataset_attribute):
    velocity = []
    for i in range(particle_amount):
        velocity_element = []
        for j in range (dataset_attribute):
            velocity_element.append(random.uniform(0,1))
        velocity.append(velocity_element)
    return velocity