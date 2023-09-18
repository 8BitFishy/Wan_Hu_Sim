import math



def Populate_List(length1, filling, length2 = None):

    list = []

    if length2 is None:
        for i in range(length1):
            list.append(filling)
    else:
        sub_list = []
        for i in range(length1):
            for j in range(length2):
                sub_list.append(filling)
            list.append(sub_list)

    return list



def Get_Force(actor1, actor2):
    G = 0.00000000006674
    #print(f"Actor 1 coords = {actor1.coords}")
    #print(f"Actor 2 coords = {actor2.coords}")

    r_x = actor2.coords[0] - actor1.coords[0]
    r_y = actor2.coords[1] - actor1.coords[1]

    r = math.sqrt(abs(r_x**2 + r_y**2))

    force = G * (actor1.mass * actor2.mass)/((r**2))

    forces = Vectorise(force, r_x, r_y)
    #print(f"x separation = {r_x}, y separation = {r_y}, r = {r}, mass 1 = {actor1.mass}, mass 2 = {actor2.mass}, force = {force}, force_vector = {forces}")
    return forces


def Vectorise(magnitude, x, y):

    if x != 0:
        angle = math.atan(abs(y/x))
    elif y >= 0:
        angle = math.pi * 0.5
    else:
        angle = math.pi * 1.5

    force_x = math.cos(angle) * magnitude
    force_y = math.sin(angle) * magnitude
    if x < 0:
        force_x = -force_x
    if y < 0:
        force_y = -force_y
    forces = [force_x, force_y]
    return forces


def Get_Sum_Of_Forces(forces):

    sum_of_forces = Populate_List(len(forces[0]), 0)


    for c in range(len(forces[0])):
        for k in range(len(forces)):
            sum_of_forces[c] += forces[k][c]


    #print(f"Force vector = {sum_of_forces}")
    return sum_of_forces


def Get_Acceleration(forces, actor1):

    acceleration = Populate_List(len(forces), 0)

    for c in range(len(forces)):
        acceleration[c] = forces[c]/actor1.mass

    #print(f"Acceleration vector = {acceleration}")

    return acceleration


def Get_Velocity(actor, acceleration):
    #print(f"Current velocity vector = {actor.velocity}")
    for c in range(len(acceleration)):
        actor.velocity[c] = (actor.velocity[c] + acceleration[c])
    #print(f"New velocity vector = {actor.velocity}")

    return actor


def Get_Coords(actor, timestep):
    #print(f"Old coordinates = {actor.coords}")

    for c in range(len(actor.coords)):
        actor.new_coords[c] = actor.coords[c] + (actor.velocity[c] * timestep)

    #print(f"New coordinates = {actor.new_coords} from v = {actor.velocity} and t = {timestep}")
    return actor