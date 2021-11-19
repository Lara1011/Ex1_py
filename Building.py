class Building:
    def __init__(self, Building):
        self.getMinFloor = Building['_minFloor']
        self.getMaxFloor = Building['_maxFloor']
        # this elev List holds the info for each elevator in this building
        self.elev = []

    def __str__(self):
        string = "Min Floor: ", self.getMinFloor, ", Max floor: ", self.getMaxFloor, ", List of elevators: ", self.elev
        return string
