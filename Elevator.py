import pandas as pd
import numpy as np
import Building

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
        # this call List holds the calls for this elevator
        self.call = []

    def __str__(self):
        string = "ID: " , self.getID , ", Speed: " , self.getSpeed, ", Min floor: " ,self.getMinFloor, ", Max floor: " ,self.getMaxFloor, ", Time for close: " ,self.getTimeForClose ,", Time for open: " , self.getTimeForOpen,\
                 ", Start time: " ,self.getStartTime, ", Stop time: " , self.getStopTime

    def travelTime(self, src, dest):
        time = self.getTimeForClose + self.getStartTime + (abs(src - dest) / self.getSpeed) \
               + self.getStopTime + self.getTimeForOpen
        return time



