import math
from random import randint, choice

global gravitational_constant
gravitational_constant = 0.00000000006674

class Actor():
    def __init__(self,name, actor_type, size, coords, vector, velocity, mass):
        self.name = name
        self.actor_type = actor_type
        self.size = size
        self.coords = coords
        self.vector = vector
        self.velocity = velocity
        self.mass = mass

    def calculate_forces(self):
        return

    def calculate_acceleration(self):
        return

    def calculate_velocity(self):  #
        return

    def calculate_coords(self):
        return


class Planet(Actor):
    def __init__(self, name, actor_type, size, coords, vector, velocity, mass, density, orbiting, orbital_radius):
        super().__init__(name, actor_type, size, coords, vector, velocity, mass)
        self.density = density
        self.orbiting = orbiting
        self.orbital_radius = orbital_radius


class Rocket:
    def __init__(self, name, actor_type, size, coords, vector, velocity, mass, thrust_vector, fuel, thrust_force):
        super().__init__(name, actor_type, size, coords, vector, velocity, mass)
        self.thrust_vector = thrust_vector
        self.fuel = fuel
        self.thrust_force = thrust_force


class Solar_System:
    def __init__(self, dims):
        self.dims = dims
        self.bodies = self.Generate_Solar_System()



    def Generate_Solar_System(self):

        new_solar_system = []
        planet_count = randint(1, 5)
        Star = self.Generate_Star()
        new_solar_system.append(Star)

        for i in range(planet_count):

            New_Planet = self.Generate_Planet(i, Star, planet_count)
            new_solar_system.append(New_Planet)

            moon_count = [0, 1, 2, 3]

            for j in range(choice(moon_count)):
                New_Satellite = self.Generate_Satellite(i, j, New_Planet)
                new_solar_system.append(New_Satellite)

        return new_solar_system



    def Generate_Satellite(self, i, j, New_Planet):

        name = f"Moon {i}-{j}"
        actor_type = "Satellite"
        size = randint(5, int(New_Planet.size/2))
        coords = [int(self.dims[0]/2), int(self.dims[1]/2)]
        vector = 0
        velocity = 0
        mass = randint(1, int(New_Planet.size/2))
        density = mass/size
        orbiting = New_Planet.name
        orbital_radius = 2

        New_Satellite = Planet(name, actor_type, size, coords, vector, velocity, mass, density, orbiting, orbital_radius)

        return New_Satellite



    def Generate_Planet(self, i, Star, planet_count):

        name = f"Planet {i}"
        actor_type = "Planet"
        size = randint(10, 44)
        mass = randint(10, 40)
        density = mass/size
        orbiting = Star.name

        orbit_midline = (i+1) * (self.dims[0] / planet_count)
        orbital_radius = randint(int(0.9*orbit_midline), (int(1.1*orbit_midline)))
        print(orbital_radius)
        velocity = math.sqrt((gravitational_constant*Star.mass)/orbital_radius)
        x_coord = Star.coords[0] + orbital_radius*math.cos(int(math.radians(randint(0, 360))))
        y_coord = Star.coords[1] + orbital_radius*math.sin(int(math.radians(randint(0, 360))))

        coords = [x_coord, y_coord]
        vector = []


        New_Planet = Planet(name, actor_type, size, coords, vector, velocity, mass, density, orbiting, orbital_radius)

        return New_Planet


    def Generate_Star(self):

        name = "Star"
        actor_type = "Star"
        size = 100
        coords = [self.dims[0]/2, self.dims[1]/2]
        vector = 0
        velocity = 0
        mass = 100
        density = mass/size
        orbiting = None
        orbital_radius = 0

        Star = Planet(name, actor_type, size, coords, vector, velocity, mass, density, orbiting, orbital_radius)

        return Star







if __name__ == '__main__':


    #TODO initiate the game
    #welcome messages etc
    #generate_map
    Space_Dims = [5000, 5000]

    #TODO generate the solar system

    solar_system = Solar_System(Space_Dims)

    p=0
    s=0
    for item in solar_system.bodies:
        print(f"{item.name} generated orbiting {item.orbiting}")
        if item.actor_type == "Planet":
            p+=1
        elif item.actor_type == "Satellite":
            s+=1

    print(f"Generated a {p} planet, {s} moon solar system")



    #TODO player launches rocket

    #TODO Run simulation