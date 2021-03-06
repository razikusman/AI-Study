class Jug:
    capacity = 0
    current_volume = 0
    name = 'new jug'

    def __init__(self, capacity, name):
        self.capacity = capacity
        self.name = name
        self.current_volume = 0

    def fill(self):
        self.current_volume = self.capacity

    def is_full(self):
        return self.current_volume == self.capacity

    def is_empty(self):
        return self.current_volume == 0

    def dump(self):
        self.current_volume = 0

    def has_target(self, target):
        return self.current_volume == target

    def transfer(self, target_jug):

        target = min(target_jug.capacity,
                            (target_jug.current_volume + self.current_volume))
        
        self_volume = max(0, target_jug.current_volume +
                       self.current_volume - target_jug.capacity)
        
        self.current_volume = self_volume
        target_jug.current_volume = target

        return True

    def transfers(self, target_jug):
    
        target = min(target_jug.capacity,
                            (target_jug.current_volume + self.current_volume))
        
        self_volume = max(0, target_jug.current_volume +
                       self.current_volume - target_jug.capacity)
        
        self.current_volume = self_volume
        target_jug.current_volume = target

        return True