import math
from random import randint
global G
import matplotlib.pyplot as plt

G = 0.00000000006674 * 100000000000
sim_speed = 1

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



def Set_Starting_Orbit(satellite_count, dimension, i):
    #print(f"Generating Orbital Radius using i = {i}, dim = {dimension}, count = {satellite_count+1}")

    #roughly even spread of orbits across system dimension
    orbit_midline = (i + 1) * (dimension / (satellite_count+1))
    #print(f"Orbital midline = {orbit_midline}")

    #orbital radius randomisation (10% either way)
    orbital_radius = randint(int(0.9 * orbit_midline), (int(1.1 * orbit_midline)))

    #print(f"Orbital radius of {orbital_radius} generated")

    return orbital_radius


def Set_Starting_Coords(orbital_focus, orbital_radius):

    #print(f"Generating starting coords using orbital focus coords {orbital_focus.coords}, orbital radius {orbital_radius}")

    # calculate coordinates of a starting point along the orbital path
    random_angle = int(math.radians(randint(0, 360)))
    x_coord = orbital_focus.coords[0] + orbital_radius * math.cos(random_angle)
    y_coord = orbital_focus.coords[1] + orbital_radius * math.sin(random_angle)
    coords = [x_coord, y_coord]
    #print(f"Coords {coords} generated")

    return coords


def Set_Starting_Velocity_Vector(coords, orbital_focus, orbital_radius):
    #print(f"Generating starting velocity vector using coords {coords}, orbital focus coords {orbital_focus.coords}, orbital focus mass {orbital_focus.mass}, orbital radius {orbital_radius}")

    #calculate the velocity (assuming circular orbit) using kepler equation
    velocity = math.sqrt((G * orbital_focus.mass) / orbital_radius)
    #print(f"Velocity {velocity} generated")

    x_offset = coords[0] - orbital_focus.coords[0]
    y_offset = coords[1] - orbital_focus.coords[1]
    #print(f"x_offset = {x_offset}, y_offset = {y_offset}")

    if x_offset == 0 or y_offset == 0:
        if y_offset == 0:
            if x_offset > 0:
                vector = [0, 1]
            else:
                vector = [0, -1]

        else:
            if y_offset > 0:
                vector = [-1, 0]
            else:
                vector = [1, 0]

    else:
        m1 = y_offset / x_offset
        m2 = -1/m1
        vector = [1, m2]
        #print(f"Gradient of radius {m1}")
        #print(f"Gradient of velocity vector {m2}")



    #print(f"Velocity vector {vector} generated")
    vector_sum = vector[0] + vector[1]
    #print(f"Velocity sum {vector_sum} generated")
    velocity_scaler = velocity / vector_sum
    #print(f"Velocity scaler {velocity_scaler} generated")
    velocity = [vector[0]*velocity_scaler, vector[1]*velocity_scaler]
    #print(f"Velocity {velocity} generated")

    return velocity


def Set_Starting_Values(orbital_focus, satellite_count, dimension, i):
    #generate an orbital radius
    orbital_radius = Set_Starting_Orbit(satellite_count, dimension, i)
    #generate starting coordinates along the orbital path
    coords = Set_Starting_Coords(orbital_focus, orbital_radius)
    #calculate orbital velocity based on the above
    velocity = Set_Starting_Velocity_Vector(coords, orbital_focus, orbital_radius)

    return coords, velocity





def run_sim(body_list, field):

    timestep = sim_speed
    total_steps = 1000

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)


    for t in range(total_steps):
        #print(f"\n\nTimestep {t}")

        for i in range(len(body_list)):
            #print(f"\nMoving {body_list[i].name}")

            if body_list[i].actor_type != "Star":

                body_list[i].coords = body_list[i].new_coords

                forces = []
                acceleration = []

                for j in range(len(body_list)):
                    if i != j:
                        ##print(f"Getting force of {body_list[j].name}")
                        forces.append(Get_Force(body_list[i], body_list[j]))

                ##print(f"Getting sum of forces")
                sum_of_forces = Get_Sum_Of_Forces(forces)

                acceleration = Get_Acceleration(sum_of_forces, body_list[i])

                body_list[i] = Get_Velocity(body_list[i], acceleration)


                body_list[i] = Get_Coords(body_list[i], timestep)
                print(f"{body_list[i].name} - coords = {body_list[i].coords}, v = {body_list[i].velocity}")


            else:
                body_list[i].new_coords = body_list[i].coords

        if (t) % 5 == 0:

            clear = True
        else:
            clear = False

        plot_bodies(body_list, field, fig, ax, clear)




def plot_bodies(body_list, field, fig, ax, clear):

    field_multiplier = 0.5
    if clear:
        ax.clear()


    for i in range(len(body_list)):
        if body_list[i].actor_type == "Star":
            colour = "red"
        elif body_list[i].actor_type == "Satellite":
            colour = "yellow"
        else:
            colour = "blue"

        ax.scatter(body_list[i].coords[0], body_list[i].coords[1], color=colour)



    plt.xlim(-field[0]*field_multiplier, field[0]*field_multiplier)
    plt.ylim(-field[0]*field_multiplier, field[1]*field_multiplier)
    fig.canvas.draw()
    fig.canvas.flush_events()