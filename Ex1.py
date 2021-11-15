import pandas as pd
import numpy as np

class Elevator:
    def __init__(self, Elevator):
        self.getID = Elevator['_id']
        self.getSpeed = Elevator['_speed']
        self.getMinFloor = Elevator['_minFloor']
        self.getMaxFloor = Elevator['_maxFloor']
        self.getTimeForClose = Elevator['_closeTime']
        self.getTimeForOpen = Elevator['_openTime']
        self.getStartTime = Elevator['_startTime']
        self.getStopTime = Elevator['_stopTime']
        self.call = []



class Building:
    def __init__(self,Building):
        self.getMinFloor = Building['_minFloor']
        self.getMaxFloor = Building['_maxFloor']
        self.elev = []

    def str(self):
        s = "minFloor: ", self.getMinFloor, ", maxFloor: ", self.getMaxFloor, ", numOfElevators: ", len(self.elev)
        return s
