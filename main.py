import Generate_Solar_System
import matplotlib.pyplot as plt
import Logger
import Physics_Engine




if __name__ == '__main__':

    logger = Logger.Generate_Logger("logs.txt")

    parameters = {}

    with open("Parameters.txt") as f:
        for line in f:
            if not line in ['\n', '\r\n']:
                name, value = line.split(":")
                name = name.rstrip(" ")
                try:
                    parameters[name] = int(value.rstrip('\n '))
                except ValueError:
                    try:
                        parameters[name] = float(value.rstrip('\n '))
                    except ValueError as e:
                        print(f"parameter file incorrect")
                        print(e)
                        exit()

    parameters["G"] = parameters["G"] * parameters["G_scalar"]
    #plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)


    #TODO initiate the game
    #welcome messages etc
    #generate_map
    Space_Dims = [5000, 5000]



    #TODO generate the solar system

    solar_system, logger = Generate_Solar_System.Generate_Solar_System(Space_Dims, logger, parameters)

    p=0
    s=0

    for item in solar_system.bodies:
        print(f"{item.name} generated")
        if item.actor_type == "Planet":
            p+=1
        elif item.actor_type == "Satellite":
            s+=1

    print(f"Generated a {p} planet, {s} moon solar system")
    Physics_Engine.run_sim(solar_system.bodies, solar_system.dims, logger, parameters)

    #plot_bodies(solar_system.bodies, solar_system.dims, fig, ax)

    #todo launch solar system simulation

    #TODO player launches rocket

    #TODO Run simulation