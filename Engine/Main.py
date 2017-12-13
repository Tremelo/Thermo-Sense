import os as os
import time as t
import datetime as dt
import random as rand #just for testing


Last_Run = None
Run_Time = 0


#function for grabbing the temperature
def Get_Temperature():
        #ideally here we would be reading the hardware sensor, for testing I've got random temp generation
        return rand.randint(50,95)
        
#Function for grabbing acceptable criteria
def Return_Threshold():
        Threshold = []
        Threshold.append(65)    #lower threshold, we will be getting these from the db
        Threshold.append(68)    #higher threshold
        
        return Threshold

#Function for getting Schedule_ID for the database
def Return_Schedule():
        return rand.randint(1,7)

#Function for changing temperature




#Function for recording stats
def Record_Statistics(temp):
        #after I set up a local mysql database, I'll mark items down.
        print(dt.datetime.fromtimestamp(t.time()).strftime('%Y-%m-%d %H:%M:%S'))
        print(temp)
        #will be logging, not just printing


#Main function for running minute updates
def Main():
        #local variables
        Last_Run = None
        Run_Time = 0
        wait_time = 5
        in_time_out = False
        
        while True:
                i = Get_Temperature()
                target = Return_Threshold()
                
                if i < target[0] and not in_time_out:
                    if Last_Run is not None:
                            Run_Time = RunTime + wait_time
                    else:
                            Last_Run = t.time()
                    
                    print("Too cold motherfucker") #Call heat protocol
                    
                elif i > target[1] and not in_time_out:
                    print("Too hot motherfucker")  #Call cool protocol
                else:
                    Run_time = 0
                    Last_Run = None
                    print("GoooOOOOOoodd")         #Do nothing Jon Snow

                Record_Statistics(i)

                #change to check every minute (right now coded for 5 seconds)
                t.sleep(wait_time)
                
                
                
                
#Actually calls running the main program                
Main()
                



