import pandas as pd
import numpy as np


class Building:
    def __init__(self,Building):
        self.getMinFloor = Building['_minFloor']
        self.getMaxFloor = Building['_maxFloor']
        # this elev List holds the info for each elevator in this building
        self.elev = []

    def __str__(self):
        string = "Min Floor: ", self.getMinFloor, ", Max floor: ", self.getMaxFloor, ", List of elevators: ", self.elev
        return string

    """    def __str__(self):
            st = "minFloor = {} maxFloor = {} ".format(self.getMinFloor, self.getMaxFloor)
            st += "elevators = {"
            for elev in self.elev:
                st+=elev.toString()
            return st + "}"
    """