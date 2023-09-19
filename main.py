import Generate_Solar_System
import matplotlib.pyplot as plt

import Physics_Engine


def plot_bodies_2(body_list):


    for i in range(len(body_list)):
        if body_list[i].actor_type == "Star":
            colour = "red"
        elif body_list[i].actor_type == "Satellite":
            colour = "yellow"
        else:
            colour = "blue"

        plt.scatter(body_list[i].coords[0], body_list[i].coords[1], color=colour)

        line_x_coords = [body_list[i].coords[0], (body_list[i].coords[0] + body_list[i].velocity[0])]
        line_y_coords = [body_list[i].coords[1], (body_list[i].coords[1] + body_list[i].velocity[1])]

        plt.plot(line_x_coords, line_y_coords, color = colour)


    plt.show()
    #fig.canvas.flush_events()







if __name__ == '__main__':

    #plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)


    #TODO initiate the game
    #welcome messages etc
    #generate_map
    Space_Dims = [50000, 50000]

    #TODO generate the solar system

    solar_system = Generate_Solar_System.Solar_System(Space_Dims)

    p=0
    s=0

    for item in solar_system.bodies:
        print(f"{item.name} generated")
        if item.actor_type == "Planet":
            p+=1
        elif item.actor_type == "Satellite":
            s+=1

    print(f"Generated a {p} planet, {s} moon solar system")

    Physics_Engine.run_sim(solar_system.bodies, solar_system.dims)

    #plot_bodies(solar_system.bodies, solar_system.dims, fig, ax)

    #todo launch solar system simulation

    #TODO player launches rocket

    #TODO Run simulation