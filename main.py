import Generate_Solar_System



if __name__ == '__main__':


    #TODO initiate the game
    #welcome messages etc
    #generate_map
    Space_Dims = [5000, 5000]

    #TODO generate the solar system

    solar_system = Generate_Solar_System.Solar_System(Space_Dims)

    p=0
    s=0

    for item in solar_system.bodies:
        print(f"{item.name} generated orbiting {item.orbiting}")
        if item.actor_type == "Planet":
            p+=1
        elif item.actor_type == "Satellite":
            s+=1

    print(f"Generated a {p} planet, {s} moon solar system")

    #todo launch solar system simulation

    #TODO player launches rocket

    #TODO Run simulation