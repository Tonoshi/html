class Planet:
    def __init__(self, data):
        self.name = data['name']
        self.rotation_period = data["rotation_period"]
        self.orbital_period = data["orbital_period"]
        self.diameter = data["diameter"]
        self.climate = data["climate"]
        self.gravity = data["gravity"]
        self.terrain = data["terrain"]
        self.surface_water = data["surface_water"]
        self.population = data["population"]
