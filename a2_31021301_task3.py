"""
# PYTHON TASK 3
# Assignment 2 - FIT9136
# Student ID : 31021301
# Created on Fri May 27 2020
# Author: Akshaya Kumar Chandrasekaran
# Last modified : 04-06-2020
#
#Importing from task3
#In this py file, I am creating a function to plot the output
#from the task 2 run_simulation() function.
#X - Axis contains the number of days
#Y - axis is the count of contagious person/patient

#This py file has visual_curve(),user_input() function.
"""


"""
From the graphs generated, it can be clearly seen that the higher the probability of meeting 
the spread of the disease is exponential and vice versa. 

There is a variation in the graph every time despite the same value is passed. 
The reason being, since the meet is based on the probability, there is  always a chance of meet happening and
a chance of meet not happening.  

Although most of the times the simulation results are matching with the predictions, the results are at times 
different than expected

eg: 
In scenario C in images try 1 and try 3, the disease continues to spread through people 
while in try 2 and try 4 the spread of disease is controlled. 

In Scenario B, in images try 2,3 and 4, we can clearly see that there is spread of the disease
 while in image try 1, the spread of the disease is controlled.

The above situation is because the probability of meeting is very low. 

But in Scenario A, in all the images shows exponential increase in the spread of disease since 
the meeting probability is greater than 0.5 (50%)
"""

# Importing from task 2 and matplotlib to generate a graph
from a2_31021301_task2 import *
import matplotlib.pyplot as plt


# visual_curve is a function that takes in three arguments from the user.
# three arguments  are 1.days, 2. meeting propability and
# 3 patient_zero_health.
# days - no of days the simulation should run
# meeting propability - probability of meeting happening
# patient_zero_health - first patient's health
# THis inturns calls the method defined in task 2 run_simulation and the
# results from the function is stored and graph is generated.

def visual_curve(days, meeting_probability, patient_zero_health):
    # calling the run_simulation() function from TASK 2 with aruguments received
    # from the user.

    list_count_days = run_simulation(days, meeting_probability, patient_zero_health)

    # Based on the results got from the simulation, a graph is generated.
    y = list_count_days
    x = range(days)
    plt.title('Contagious Spread Curve')
    plt.plot(x, y, '-o')
    plt.xlabel('days')
    plt.ylabel('count')
    #plt.title('Scenario_A || 30_0.6_25')
    #plt.savefig('Scenario_A-try 1')
    plt.show()


# user_input is a function that asks inputs from user and calls the visual_curve function to
# Generate graphs
def user_input():
    try:
        # Asking user to input the number of days the simulation should run.
        no_of_days = int(input("Enter the number of days to run simulation : "))

        # If the number of days is less than or equal to 0, asking to re-enter
        while (no_of_days <= 0):
            print("Number of days cannot be less than or equal to '0'\n")
            no_of_days = int(input("Enter the number of days to run simulation : "))

        # Asking user to input the meeting probabilty event happening .
        meet_prob = float(input("Enter number between 0.0 and 1.0(Probability value) : "))

        # If the number of days is less than 0 or more than 1, asking to re-enter
        while (meet_prob < 0 or meet_prob > 1):
            print("Probability value should be 0 to 1 ")
            meet_prob = float(input("Enter number between 0.0 and 1.0(Probability value) : "))

        # Asking user to input the Patient health .
        patient_health = float(input("Enter first Patient's health : "))

        # If the number of days is less than 0 or more than 100, asking to re-enter
        while (patient_health < 0 or patient_health > 100):
            print("Patient health should be between 0 and 100")
            patient_health = float(input("Enter first Patient's health : "))

        patient_health = round(patient_health)

        # Calling the function definition
        visual_curve(no_of_days, meet_prob, patient_health)
    except ValueError:
        print(
            "Please enter only Interger for Number of Days, float for Probabilty and float or integer for patient's health")
        checkInput = input("Want to enter correct Values and try again? Press 1 \n Else press any key to quit: ")
        if (checkInput == '1'):
            user_input()


if __name__ == '__main__':
    user_input()

# do not add code here (outside the main block).
