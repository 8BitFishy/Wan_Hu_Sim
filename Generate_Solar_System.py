from random import randint, choice
import math
import Physics_Engine

class Solar_System:
    def __init__(self, dims):

        #general rules of the universe
        self.dims = dims

        #generate celestial bodies and attach as attributes
        self.bodies = []







    def Generate_Body(self, actor_type, i, logger, parameters, j = None, count = None, orbital_focus = None, a=None, m1=None, M2=None):
        orbit_adjuster = [0, 0]
        if actor_type == "Star":
            name = "Star"
            actor_type = "Star"
            size = 100
            coords = [0, 0]
            velocity = [0, 0]
            mass = parameters["star_mass"]

            body_number = i

        else:
            if actor_type == "Satellite":
                name = f"Moon {i}-{j}"
                actor_type = "Satellite"
                size = randint(5, int(orbital_focus.size / 2))
                mass = parameters["satellite_mass"]
                hill_sphere_radius = a * (m1/(3*M2))**(1/3)
                dimension = hill_sphere_radius * 0.8
                print(f"a = {a}, m = {m1}, M = {M2}, hill sphere radius = {hill_sphere_radius}")
                logger.Write_To_Log(f"a = {a}, m = {m1}, M = {M2}, hill sphere radius = {hill_sphere_radius}")
                orbit_adjuster = orbital_focus.velocity
                body_number = j


            else:
                actor_type == "Planet"
                name = f"Planet {i}"
                actor_type = "Planet"
                size = randint(10, 44)
                mass = parameters["planet_mass"]
                dimension = self.dims[0]/2
                body_number = i


            print(f"Running physics engine calcs...")
            coords, velocity, logger = Physics_Engine.Set_Starting_Values(orbital_focus, count, dimension, body_number, logger, parameters["G"])

            velocity[0] = velocity[0] + orbit_adjuster[0]
            velocity[1] = velocity[1] + orbit_adjuster[1]

        New_Body = Planet(name, actor_type, size, coords, velocity, mass)
        print(f"New {New_Body.actor_type} generated with size {New_Body.size}, coords {New_Body.coords}, velocity {New_Body.velocity}, mass {New_Body.mass}")
        logger.Write_To_Log(f"New {New_Body.actor_type} generated with size {New_Body.size}, coords {New_Body.coords}, velocity {New_Body.velocity}, mass {New_Body.mass}")
        return New_Body, logger


class Actor():
    def __init__(self,name, actor_type, size, mass, coords=[0, 0], velocity=[0, 0]):
        self.name = name
        self.actor_type = actor_type
        self.size = size
        self.coords = coords
        self.new_coords = coords
        self.velocity = velocity
        self.mass = mass


class Planet(Actor):
    def __init__(self, name, actor_type, size, coords, velocity, mass):
        super().__init__(name, actor_type, size, mass, coords, velocity)



class Rocket:
    def __init__(self, name, actor_type, size, coords, vector, velocity, mass, thrust_vector, fuel, thrust_force):
        super().__init__(name, actor_type, size, coords, vector, velocity, mass)
        self.thrust_vector = thrust_vector
        self.fuel = fuel
        self.thrust_force = thrust_force



def Generate_Solar_System(Space_Dims, logger, parameters):

    new_solar_system = Solar_System(Space_Dims)

    #new_solar_system list holds bodies
    #new_solar_system = []
    #planet_count here
    planet_count = parameters["planet_count"]
    max_moons_per_planet = parameters["satellite_count"]
    #star count here
    star_count = parameters["star_count"]
    logger.Write_To_Log(f"Generating a {star_count} star system with {planet_count} planets")
    print(f"Generating a {star_count} star system with {planet_count} planets")


    #Generate stars and append to list
    for s in range(star_count):
        print(f"\n\nGenerating Star {s}")
        logger.Write_To_Log(f"\n\nGenerating Star {s}")
        Star, logger = new_solar_system.Generate_Body("Star", s, logger, parameters)
        new_solar_system.bodies.append(Star)


    #generate planets
    for i in range(planet_count):
        print(f"\n\nGenerating Planet {i}")
        logger.Write_To_Log(f"\nGenerating Planet {i}")

        #todo update orbital foci to accomodate binary systems
        New_Planet, logger = new_solar_system.Generate_Body("Planet", i, logger, parameters, count=planet_count, orbital_focus=Star)
        new_solar_system.bodies.append(New_Planet)

        moon_count = randint(max_moons_per_planet, max_moons_per_planet)
        print(f"Generating {moon_count} moons for {New_Planet.name}")
        logger.Write_To_Log(f"Generating {moon_count} moons for {New_Planet.name}")

        for j in range(moon_count):
            print(f"\nGenerating Moon {i}-{j}")
            logger.Write_To_Log(f"\nGenerating Moon {i}-{j}")

            a = math.sqrt(abs((Star.coords[0]-New_Planet.coords[0]))**2 + abs((Star.coords[1]-New_Planet.coords[1]))**2)
            m1 = New_Planet.mass
            M2 = Star.mass

            New_Satellite, logger = new_solar_system.Generate_Body("Satellite", i, logger, parameters, j, count=planet_count, orbital_focus=New_Planet, a=a, M2=M2, m1=m1)
            new_solar_system.bodies.append(New_Satellite)

    #return list of bodies
    return new_solar_system, logger