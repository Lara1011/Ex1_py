import pandas as pd
import numpy as np

class CallForElevator:
    def __init__(self,CallForElevator):
        # The time the person called the elevator.
        self.getTime = CallForElevator['time']
        # The source floor(the person's floor)
        self.getSrc = CallForElevator['source']
        # The destination floor(goto)
        self.getDest = CallForElevator['destination']
        # Returns the elevator's direction (UP/DOWN)
        self.getState = CallForElevator['flag']
        # The index of the elevator that answers the call
        self.AllocatedTo = CallForElevator['elevator_index']