from random import randint, choice
import math
import Physics_Engine

class Solar_System:
    def __init__(self, dims):

        #general rules of the universe
        self.dims = dims

        #generate celestial bodies and attach as attributes
        self.bodies = self.Generate_Solar_System()




    def Generate_Solar_System(self):

        #new_solar_system list holds bodies
        new_solar_system = []
        #planet_count here
        planet_count = 1
        max_moons_per_planet = 3
        #star count here
        star_count = 1

        print(f"Generating a {star_count} star system with {planet_count} planets")


        #Generate stars and append to list
        for s in range(star_count):
            print(f"\n\nGenerating star {s}")
            Star = self.Generate_Body("Star", s)
            new_solar_system.append(Star)

        #generate planets
        for i in range(planet_count):
            print(f"\n\nGenerating planet {i} with orbital focus = {Star.name}")
            #todo update orbital foci to accomodate binary systems
            New_Planet = self.Generate_Body("Planet", i, count=planet_count, orbital_focus=Star)
            new_solar_system.append(New_Planet)

            #generate satellites for new planet
            moon_count = randint(0, max_moons_per_planet)
            print(f"Generating {moon_count} moons for {New_Planet.name}")

            for j in range(moon_count):
                print(f"\nGenerating moon {j}")
                New_Satellite = self.Generate_Body("Satellite", i, j, count=planet_count, orbital_focus=New_Planet)
                new_solar_system.append(New_Satellite)

        #return list of bodies
        return new_solar_system


    def Generate_Body(self, actor_type, i, j = None, count = None, orbital_focus = None):
        orbit_adjuster = [0, 0]
        if actor_type == "Star":
            name = "Star"
            actor_type = "Star"
            size = 100
            coords = [0, 0]
            velocity = [0, 0]
            mass = 1000000000
            body_number = i

        else:
            if actor_type == "Satellite":
                name = f"Moon {i}-{j}"
                actor_type = "Satellite"
                size = randint(5, int(orbital_focus.size / 2))
                mass = 10000
                dimension = self.dims[0] / 10
                orbit_adjuster = orbital_focus.velocity
                body_number = j


            else:
                actor_type == "Planet"
                name = f"Planet {i}"
                actor_type = "Planet"
                size = randint(10, 44)
                mass = 100000000
                dimension = self.dims[0]/2
                body_number = i


            print(f"Running physics engine calcs...")
            coords, velocity = Physics_Engine.Set_Starting_Values(orbital_focus, count, dimension, body_number)

            velocity[0] = velocity[0] + orbit_adjuster[0]
            velocity[1] = velocity[1] + orbit_adjuster[1]

        New_Body = Planet(name, actor_type, size, coords, velocity, mass)
        print(f"New {New_Body.actor_type} generated with size {New_Body.size}, coords {New_Body.coords}, velocity {New_Body.velocity}, mass {New_Body.mass}")

        return New_Body


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
