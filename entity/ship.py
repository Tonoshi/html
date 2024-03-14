class Ship:
    def __init__(self, data):
        self.name = data['name']
        self.model = data['model']
        self.manufacturer = data['manufacturer']
        self.cost_in_credits = data['cost_in_credits']
        self.length = data['length']
        self.max_atmosphering_speed = data['max_atmosphering_speed']
