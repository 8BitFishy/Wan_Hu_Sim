import math
from random import randint
import matplotlib.pyplot as plt

class Body():
    def __init__(self, coords, mass, velocity):
        self.coords = coords
        self.new_coords = coords
        self.mass = mass
        self.velocity = velocity

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





def run_sim(body_list, field):

    timestep = 1
    total_steps = 1000

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)


    for t in range(total_steps):
        #print(f"\n\nTimestep {t}")

        for i in range(len(body_list)):
            #print(f"\nMoving body {i}")

            body_list[i].coords = body_list[i].new_coords

            forces = []
            acceleration = []

            for j in range(len(body_list)):
                if i != j:
                    #print(f"Getting force of body {j}")
                    forces.append(Get_Force(body_list[i], body_list[j]))

            #print(f"Getting sum of forces")
            sum_of_forces = Get_Sum_Of_Forces(forces)

            acceleration = Get_Acceleration(sum_of_forces, body_list[i])

            body_list[i] = Get_Velocity(body_list[i], acceleration)
            if i != 0:
                body_list[i] = Get_Coords(body_list[i], timestep)
                #print(f"Body {i} - v = {body_list[i].velocity}, coords = {body_list[i].coords}")
                pass
            else:
                body_list[i].new_coords = body_list[i].coords

        plot_bodies(body_list, field, fig, ax)


def generate_bodies(field):

    starting_velocity_scalar = 100
    body_count = 100
    body_list = []

    for i in range(body_count):
        mass = 100000000000000000
        starting_positions = []

        while True:
            starting_position = [randint(-field[0], field[0]), randint(-field[1], field[1])]
            if starting_position in starting_positions:
                continue
            else:
                break

        starting_velocity = [randint(-starting_velocity_scalar, starting_velocity_scalar), randint(-starting_velocity_scalar, starting_velocity_scalar)]

        if i == 0:
            mass = mass*100
            starting_velocity = [0, 0]
            starting_position = [0, 0]

        new_body = Body(starting_position, mass, starting_velocity)
        #print(f"Generated new body {i} with starting position {starting_position} and v = {starting_velocity}")

        body_list.append(new_body)

    return body_list





def plot_bodies(body_list, field, fig, ax):

    field_multiplier = 1


    x_points = []
    y_points = []


    for c in range(len(body_list[0].coords)):
        for i in range(len(body_list)):
            if i != 0:
                if c == 0:
                    x_points.append(body_list[i].coords[c])
                elif c == 1:
                    y_points.append(body_list[i].coords[c])
            else:
                if c == 0:
                    star_x = body_list[i].coords[c]
                elif c == 1:
                    star_y = body_list[i].coords[c]

    ax.clear()
    ax.scatter(x_points, y_points)
    ax.scatter(star_x, star_y, c="red")
    plt.xlim(-field[0]*field_multiplier, field[0]*field_multiplier)
    plt.ylim(-field[0]*field_multiplier, field[1]*field_multiplier)
    fig.canvas.draw()
    fig.canvas.flush_events()

    return


if __name__ == '__main__':
    field = [20000, 20000]
    ##print(f"Starting Sim")
    body_list = generate_bodies(field)
    run_sim(body_list, field)
