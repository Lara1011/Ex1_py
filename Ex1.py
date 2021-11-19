import pandas as pd
from Building import Building
from Elevator import Elevator
import json

def LoadCalls(path):
    try:
        calls = pd.read_csv(path, header=None)
        return calls
    except IOError as e:
        print(e)


def LoadBuilding(path):
    try:
        with open(path, "r") as f:
            build = json.load(f)
            my_building = Building(build)
            for my_elev in build['_elevators']:
                my_building.elev.append(Elevator(my_elev))
        return my_building
    except IOError as e:
        print(e)


def LoadOutput(index, path, row):
    path.loc[row, '5'] = index
    return path


def allocateElevator(path1, path2, path3):
    myBuilding = LoadBuilding(path1)
    myOut = LoadCalls(path2)
    print(myOut)
    myOut['difference'] = abs(myOut[2] - myOut[3])
    myOut = myOut.sort_values(['difference'], ascending=True)
    myOut['RunHere'] = range(0, len(myOut))
    myOut = myOut.set_index(['RunHere'])
    numOfElev = len(myBuilding.elev)
    partition = int(len(myOut) / numOfElev)
    if numOfElev == 1:
        myOut[5] = 0
    else:
        start = 0
        stop = len(myBuilding.elev)
        for i in range(0, len(myOut), partition):
            if start < stop:
                for j in range(i, partition + i):
                    myOut.at[j, 5] = start
            start = start + 1
    myOut = myOut.drop(['difference'], axis=1)
    myOut.reset_index(drop=True, inplace=True)
    j = 0
    k = partition
    for i in myOut:
        while i < k:
            myBuilding.elev[j].call.append(myOut[2].iloc[i])
            myBuilding.elev[j].call.append(myOut[3].iloc[i])
            i = i + 1
        k = k + partition
        j = j + 1
        if len(myBuilding.elev) == j:
            break
    myOut = myOut.sort_values([1])
    myOut.to_csv(path3, index=False, header=False)
    print(myOut)

if __name__ == '__main__':
    # Run an example:
    allocateElevator(r'C:\Users\malak\OneDrive\Desktop\New folder\B1.json',
                     r'C:\Users\malak\OneDrive\Desktop\New folder\Calls_a.csv',
                     r'C:\Users\malak\OneDrive\Desktop\New folder\outputB1a.csv')
