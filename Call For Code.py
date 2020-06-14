import csv

#Assuming the person is a resting adult

# norHeart = [71,82,64,73,64,70,82,69,74]# List will constantly change with each extra input

def good_Heart(all):
    totHeart = 0
    for i in all:
        totHeart += float(i)
    avgHeart = totHeart / len(all)
    print (avgHeart)
    return avgHeart

#For Example
def abnormal_Heart(check,condition):
    newHeart = input("New heart rate: ") #Constantly gets new inputs
    if condition == "Y":
        if float(newHeart) - float(check) >= 40 or float(newHeart) - float(check) <= -40:
            print("Alert Mode")
            return "alert"#Wearable device is set to alert mode, if any life threatening symptoms appear it will activate
        else:
            return False
    else:
        if float(newHeart) > 100 or float(newHeart) < 60: #Average healthy adult heart rate should be 60-100
            print("Alert Mode")
            return "alert"#Wearable device is set to alert mode, if any life threatening symptoms appear it will activate
        else:
            return False

def problem_Check(filepath):

    with open(filepath) as csvfile:
        readCSV = csv.reader(csvfile,delimiter=',')
        for row in readCSV:
            heartrate = row

    underConditions = input("Is there underlying conditions(Y/N): ")#Checks if person has underlying heart conditions
    while True:
        if abnormal_Heart(good_Heart(heartrate),underConditions) == "alert":
            if abnormal_Heart(good_Heart(heartrate),underConditions) == "alert":#If device gets alerted 2 times in a row check if user is okay
                call = input("Respond if okay")
                if call == "": #If user is not responding after 1 minute, call will be empty
                    print("Requires help. Call the ambulance.")#Application will ping nearby people and call the ambulance.
                    return "stop"


problem_Check('normalheartbeat.csv')





