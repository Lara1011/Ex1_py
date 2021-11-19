# Ex_1
---
## Elevator Algorithm 
Our assignment is to create an offline algorithm for elevators that the average wait time is as small as possible.
We are presenting four projects that are relative to our project each of the for projects that we have found are simillar; deals with large buildings, crowded at peak times, and the idea behind each project is suitable to our project. 
1) [https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup](https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup)
2) [https://web.archive.org/web/20120718231009/http:/thyssenkruppelevator.com/destdist.asp]( https://web.archive.org/web/20120718231009/http:/thyssenkruppelevator.com/destdist.asp)
3) [https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele...](https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele...)
4) [https://www.diva-portal.org/smash/get/diva2:668671/fulltext01.pdf](https://www.diva-portal.org/smash/get/diva2:668671/fulltext01.pdf)
---
### Classes:
Our program contains 2 classesas:
- __Building__: The building pulls out the data from the Building.json files, and fill in three objects: minfloor, maxfloor and elevators list.
- __Elevator__: The elevator also pulls out its data from the Building.json files, specifically from the building elevators list that we filled.
---
### Our Algorithm:
In the `main class` we have a function called `allocateElevator` that its inputs are 3 pathes: <br>
We read the data from 3 files:
1) json file which contains data about the building as described above.
2) csv file that contains all the info about the calls: time of the call, source floor, destination floor, and the elevator the call is allocated to.
3) Another csv file, output, but this one is empty, we fill it after allocate each call to a specific elevator. 
We used a library called `pandas` to load the csv file to a dataframe and after we finished working on it, we load it into the output file.

The `algorithm` that we came up with is all about sorting the calls based on the difference between the source floor and the destination floor, then we divided the calls evenly between the elevators, so in this way each elevator gets `calls for each elevator = number of calls \ number of elevators`, the elevator in the first index of elevators list answers the calls with the smallest distance, and the elevator in the last index of the elevators list answers the calls with the biggest distance, the elevators between the first and the last index in the elevators list answers the calls in between in order.<br><br>

**For Example:** Building that has 50 floors, 5 elevators, and 500 calls, we sort the calls based on the difference in distance(from smallest to biggest), then we divide the 500 calls by the 5 elevators, in that way each elevator answers 100 calls,so elevator[0] answers the first 100 calls, elevator[1] answers the second 100 calls and so on...
After that we sort the dataframe based on the time of each call, we save the dataframe in the output csv file with the allocated elevators in it. <br>

---
## Algorithm Results:

|   	    | B1     |	B2	| B3   |	B4  |	B5   |
|---------|--------|------|------|------|------|
| Calls_a |	112.92 |48.04 | 29.2 |23.44 |22.18|
| Calls_b	|		     |      |451.18|184.03|81.33|
| Calls_c	|		     |      |486.23|175.77|78.81|
| Calls_d	|		     |      |457.29|175.44|79.08|

For buildings 1,2 we only ran calls_a because the floors are out of range.

---
## How to run & Installation:

__Install Pandas:__ 
1) Type in the command "pip install manager"
2) Once finished, type "pip install pandas"

__How To Run:__

In cmd, the main should get `java -jar Ex1_checker_V1.2_obf.jar <IDs, json, calls, log_out>`
IDs:123456789,987654321,22222222
json: a file name such as B1.json - B5.json (or any other such json)
cals: a file name to a call log such as Call_a.csv = Call_d.csv
log_out: the name of the file with all the simulation log.

---

## UML:
![Diagram](https://user-images.githubusercontent.com/75528759/142690291-5a947826-ae2a-432e-9944-bec900324452.png)

