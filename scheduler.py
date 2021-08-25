import sys
import csv 

"""
Defining each values in a class and using self helps to access these values , by creating an instance of each object and calling them 
as needed 
"""
class Process:
    def __init__ (self, ProcessID, ArrivalTime, BurstTime):
        self.ProcessID = ProcessID
        self.ArrivalTime = ArrivalTime
        self.BurstTime = BurstTime
        self.ProgressTime = 0
        self.WaitingTime = 0
        self.StartTime = -1
        self.EndTime = -1
        self.IsRunning = False

# Initialize
"""
First step is to get the input file from command line argument and extract ProcessID, ArrivalTime and BurstTime from the file 
After that convert those values from strings to integers and then append it to a an array so all the other methods can utilize the
input values. 
"""
file_name = sys.argv[1]
File = open(file_name, 'r')
TimeQuantum = int(sys.argv[2])
File.readline()
Processes = []
with open(file_name, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        ProcessID = int(line[0])
        ArrivalTime = int(line[1])
        BurstTime = int(line[2])
        Processes.append(Process(ProcessID, ArrivalTime, BurstTime))

csvContents = Processes
Times = []

#_________________________________________FirstComeFirstServe____________________________________________
"""
Loop through the contents of the file and sort the ProcessID's in asceding values and swap it 
"""
for i in range(0, len(csvContents)):
    for j in range(i + 1, len(csvContents)):
        if csvContents[i].ProcessID > csvContents[j].ProcessID:
            temp = csvContents[i]
            csvContents[i] = csvContents[j]
            csvContents[j] = temp
"""
Creating booleans helps to exit the loop easily and end a process 
Checking for wait time and then adding to the an array to be able to later accessed by .

"""
running = True
time = 0
while(running):
    progress = False

    for temp in csvContents:                        #check for the current wait time and proceed accordingly 
        if temp.IsRunning:      
            if temp.ProgressTime == temp.BurstTime:     
                temp.IsRunning = False
                temp.EndTime = time
            else:
                progress = True
                temp.ProgressTime += 1
                Times.append(str(temp.ProcessID))
    
    if not progress:
        for temp in csvContents:
            if temp.StartTime == -1 and temp.ArrivalTime <= time:
                progress = True
                temp.IsRunning = True           
                temp.StartTime = time
                temp.ProgressTime += 1
                Times.append(str(temp.ProcessID))
                break

    for temp in csvContents:
        if temp.ArrivalTime <= time and not temp.IsRunning and temp.EndTime == -1:
            temp.WaitingTime += 1
    
    if not progress:
        Times.append("IDLE")
    
    time += 1
    
    finished = 0
    for temp in csvContents:
        if temp.EndTime > 0:
            finished += 1
    if finished == len(csvContents):
        running = False



for i in range(0, len(csvContents)):
    for j in range(i + 1, len(csvContents)):
        if csvContents[i].ProcessID > csvContents[j].ProcessID:
            temp = csvContents[i]
            csvContents[i] = csvContents[j]
            csvContents[j] = temp

print("--------------------- FCFS --------------------")
print("  Process ID    | Waiting Time  | Turnaround Time")
for temp in csvContents:
    print("\t" + str(temp.ProcessID) + "\t|\t" + str(temp.WaitingTime) + "\t|\t" + str(temp.EndTime - temp.ArrivalTime))
print("Gantt Chart is:")
Result = []
Show = True
for i in range(time - 1):
    if Show:
        Result.append("[\t" + str(i) + "\t]--\t" + Times[i])
    if Times[i] == Times[i + 1]:
        Show = False
    else:
        Result.append("\t--[\t" + str(i + 1) + "\t]")
        Show = True
for i in range(0, len(Result), 2):
    print(Result[i] + Result[i + 1])
WaitingTime = 0
TurnarountTime = 0
for temp in csvContents:
    WaitingTime += temp.WaitingTime
    TurnarountTime += temp.EndTime - temp.ArrivalTime
print("Average Waiting Time: " + str(WaitingTime / len(csvContents)))
print("Average Turnarount Time: " + str(TurnarountTime / len(csvContents)))
print("Throughput: " + str(len(csvContents) / (time - 1)))

#_________________________ShortestJobFirst_____________________________________
for temp in csvContents:
    temp.ProgressTime = 0
    temp.WaitingTime = 0
    temp.StartTime = -1
    temp.EndTime = -1
    temp.IsRunning = False
Times = []

running = True
time = 0
while(running):
    tempTime = 0

    for temp in csvContents:
        if temp.ProgressTime == temp.BurstTime and temp.EndTime == -1:
            temp.EndTime = time

    for temp in csvContents:
        if temp.EndTime == -1 and temp.ArrivalTime <= time:
            if tempTime  == 0:
                tempTime = temp.BurstTime - temp.ProgressTime
            else:
                if temp.BurstTime - temp.ProgressTime < tempTime:
                    tempTime = temp.BurstTime - temp.ProgressTime

    if tempTime != 0:
        for temp in csvContents:
            if temp.EndTime == -1 and temp.ArrivalTime <= time and tempTime == temp.BurstTime - temp.ProgressTime:
                temp.IsRunning = True
                if temp.StartTime == -1:
                    temp.StartTime = time
                temp.ProgressTime += 1
                Times.append(str(temp.ProcessID))
                break
                
    else:
        Times.append("IDLE")

    for temp in csvContents:
        if temp.ArrivalTime <= time and not temp.IsRunning and temp.EndTime == -1:
            temp.WaitingTime += 1
        temp.IsRunning = False

    time += 1

    finished = 0
    for temp in csvContents:
        if temp.EndTime > 0:
            finished += 1
    if finished == len(csvContents):
        running = False

print("--------------------- SJFP --------------------")
print("  Process ID    | Waiting Time  | Turnaround Time")
for temp in csvContents:
    print("\t" + str(temp.ProcessID) + "\t|\t" + str(temp.WaitingTime) + "\t|\t" + str(temp.EndTime - temp.ArrivalTime))
print("Gantt Chart is:")
Result = []
Show = True
for i in range(time - 1):
    if Show:
        Result.append("[\t" + str(i) + "\t]--\t" + Times[i])
    if Times[i] == Times[i + 1]:
        Show = False
    else:
        Result.append("\t--[\t" + str(i + 1) + "\t]")
        Show = True
for i in range(0, len(Result), 2):
    print(Result[i] + Result[i + 1])
WaitingTime = 0
TurnarountTime = 0
for temp in csvContents:
    WaitingTime += temp.WaitingTime
    TurnarountTime += temp.EndTime - temp.ArrivalTime
print("Average Waiting Time: " + str(WaitingTime / len(csvContents)))
print("Average Turnarount Time: " + str(TurnarountTime / len(csvContents)))
print("Throughput: " + str(len(csvContents) / (time - 1)))

#______________________________________RoundRobin____________________________________________

for temp in csvContents:
    temp.ProgressTime = 0
    temp.WaitingTime = 0
    temp.StartTime = -1
    temp.EndTime = -1
    temp.IsRunning = False
Times = []

running = True
time = 0
tempTime = 0
index = 0
while(running):
    for temp in csvContents:
        if temp.ProgressTime == temp.BurstTime and temp.EndTime == -1:
            temp.EndTime = time

    progress = False
    runout = False
    index = 0

    for i in range(index, len(csvContents)):
        if csvContents[i].IsRunning:
            if tempTime == 0:
                csvContents[i].IsRunning = False
                index = i
                runout = True
            else:
                tempTime -= 1
                progress = True
                csvContents[i].ProgressTime += 1
                Times.append(str(csvContents[i].ProcessID))
            break
    if not progress:
        if runout:
            if index == len(csvContents) - 1:
                index = 0
            else:
                index += 1
        for i in range(index, len(csvContents)):
            if csvContents[i].EndTime == -1 and csvContents[i].ArrivalTime <= time:
                progress = True
                csvContents[i].IsRunning = True
                if csvContents[i].StartTime == -1:
                    csvContents[i].StartTime = time
                if TimeQuantum > (csvContents[i].BurstTime - csvContents[i].ProgressTime):
                    tempTime = csvContents[i].BurstTime - csvContents[i].ProgressTime
                else:
                    tempTime = TimeQuantum
                tempTime -= 1
                csvContents[i].ProgressTime += 1
                Times.append(str(csvContents[i].ProcessID))
                break

    if not progress:
        for i in range(0, index):
            if csvContents[i].EndTime == -1 and csvContents[i].ArrivalTime <= time:
                progress = True
                csvContents[i].IsRunning = True
                if csvContents[i].StartTime == -1:
                    csvContents[i].StartTime = time
                if TimeQuantum > (csvContents[i].BurstTime - csvContents[i].ProgressTime):
                    tempTime = csvContents[i].BurstTime - csvContents[i].ProgressTime
                else:
                    tempTime = TimeQuantum

                tempTime -= 1
                csvContents[i].ProgressTime += 1
                Times.append(str(csvContents[i].ProcessID))
                break

    if not progress:
        Times.append("IDLE")

    for temp in csvContents:
        if temp.ArrivalTime <= time and not temp.IsRunning and temp.EndTime == -1:
            temp.WaitingTime += 1
    
    time += 1
    
    finished = 0
    for temp in csvContents:
        if temp.EndTime > 0:
            finished += 1
    if finished == len(csvContents):
        running = False

print("------------------- Round Robin -----------------")
print("  Process ID    | Waiting Time  | Turnaround Time")
for temp in csvContents:
    print("\t" + str(temp.ProcessID) + "\t|\t" + str(temp.WaitingTime) + "\t|\t" + str(temp.EndTime - temp.ArrivalTime))
print("Gantt Chart is:")
Result = []
Show = True
for i in range(time - 1):
    if Show:
        Result.append("[\t" + str(i) + "\t]--\t" + Times[i])
    if Times[i] == Times[i + 1]:
        Show = False
    else:
        Result.append("\t--[\t" + str(i + 1) + "\t]")
        Show = True
for i in range(0, len(Result), 2):
    print(Result[i] + Result[i + 1])
WaitingTime = 0
TurnarountTime = 0
for temp in csvContents:
    WaitingTime += temp.WaitingTime
    TurnarountTime += temp.EndTime - temp.ArrivalTime
print("Average Waiting Time: " + str(WaitingTime / len(csvContents)))
print("Average Turnarount Time: " + str(TurnarountTime / len(csvContents)))
print("Throughput: " + str(len(csvContents) / (time - 1)))