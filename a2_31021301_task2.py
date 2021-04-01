"""
# PYTHON TASK 2
# Assignment 2 - FIT9136
# Student ID : 31021301
# Created on Fri May 25 2020
# Author: Akshaya Kumar Chandrasekaran / Co-Author : Namrata Palai
# Last modified : 04-06-2020
#
#Importing from task1
#In this py file, A patient class and objects for the class are created
#and connections are established  for the objects created.
#This py file has Patient class with methods constructor,get_health(),
#set_health(),is_contagious(),infect() and sleep()
#and a function load_patients() and run_simulation()
"""

# importing a2_31021301_task1 and random function to generate a random number
# between 0 and 1 to check the meeting probability
import random
from a2_31021301_task1 import *


# Creating Patient class and defining methods

class Patient(Person):

    # Constructor that inherits the method from the parent class Person
    # and uses it's constructor to initialise fname and lname
    # Additionally health for the patient object is initialised in this class.
    def __init__(self, first_name, last_name, health):
        super().__init__(first_name, last_name)
        self.health = health

    # To get the health of the patient
    def get_health(self):
        return self.health

    # set_health() takes one argument and sets the health of the patient to the
    # value received.
    def set_health(self, new_health):
        self.health = new_health

    # Based on the given health condition, if the health of the patient is less
    # than 50, it returns true else returns false.
    def is_contagious(self):
        if self.health < 50:
            return True
        else:
            return False

    # If the person is contagious, their connection is infected with viral load
    # which is calculated under various factors and new health for the person is
    # set based on the patient's health.

    def infect(self, viral_load):
        if (self.health >= 0 and self.health <= 100):
            if (self.health <= 29):
                day_health = self.health - (0.1 * viral_load)
                # health can never be less than 0, so checking if the health is
                # less than 0, it is set to 0.
                if (day_health < 0):
                    day_health = 0
                self.set_health(day_health)
            elif (self.health > 29 and self.health < 50):
                day_health = self.health - (1 * viral_load)
                # health can never be less than 0, so checking if the health is
                # less than 0, it is set to 0.
                if (day_health < 0):
                    day_health = 0
                self.set_health(day_health)
            else:
                day_health = self.health - (2 * viral_load)
                # health can never be less than 0, so checking if the health is
                # less than 0, it is set to 0.
                if (day_health < 0):
                    day_health = 0
                self.set_health(day_health)

    # After eevery day the patient is set to sleep which makes their health
    # increase by 5.
    def sleep(self):
        if (self.health <= 100):
            self.health = self.health + 5
        # Maximum value a patient can have is 100. IF health is greater than 100
        # then it is set to 100.
        if (self.health > 100):
            self.health = 100


# load_patient is a function that reads data from the text file given and
# saves it as a list  and takes the first person's health as its argument

# Once all the split based on the delimiter is done, A Patient object is created
# for all the unique name mentioned.

# Once Patient object for all the unique name is created, add_friend function is
# called and the connection is established by adding friends.

def load_patients(initial_health):
    # reads the file
    my_file = open("a2_sample_set.txt", "r")

    # Store values in text file as list
    name_list = my_file.readlines()

    # closing the file
    my_file.close()

    # Based on the delimiter given, spliting each line in the list
    # and creating index to get only the unique name
    # uniquelist will have [person name],[his/her friends name sep by ","]
    unique_list = []
    for i in range(len(name_list)):
        unique_list.append(name_list[i].split(': '))

    # from the uniquelist, getting only the first index to get the unique names
    # and appending it to uniquename list
    unique_name = []
    for i in range(len(unique_list)):
        unique_name.append(unique_list[i][0])

    # Friend list from the unique list is taken and first index is considered
    # while separating and added as individual index in friends list object
    frnds_list = []
    for i in range(len(name_list)):
        frnds_list.append(unique_list[i][1].strip().split(', '))

    # To create patient object and to store the same, from the unique name list,
    # first name and last name is split and passed in as two arguments as fname
    # and lname and creating person object along with the initial health for the
    # patient.

    # These objects will get saved exactly in the index as that of the unique
    # name, so that values can be compared easily and correct object is added

    patient_obj = []
    for i in range(len(unique_name)):
        fname, lname = unique_name[i].split()
        patient_obj.insert(i, Patient(fname, lname, initial_health))

    # For the length of the friend list,
    for i in range(len(frnds_list)):

        # for the length of each friend a person has
        for j in range(len(frnds_list[i])):

            # to iterate through the unique name to get the index of the
            # person we are looking for
            for temp in range(len(unique_name)):

                # only if the patient we are looking for matches with the
                # unique name, add that patient object as a connection of patient
                if (unique_name[temp] == frnds_list[i][j]):
                    patient_obj[i].add_friend(patient_obj[temp])

    # returns the list of person object
    return patient_obj


"""
#run_simulation takes three arguments 1.days, 2. meeting propability and
#3 patient_zero_health. 
#days - no of days the simulation should run
#meeting propability - probability of meeting happening
#patient_zero_health - first patient's health

#for the number of days given, iteration is ran and patient's health is 
#checked. the possibilty for a meet is checked only if the patient/ their 
# friend is contagious or not. their connections(each iteration
# through friends list) are checked if they are
#contagious or not. If any one of them is contagious, then a viral load is 
#calcualted based on the health and their health points are set accordingly.
#By the end of the day, no of contagious patients are appended to the list.
#list is returned.
"""


def run_simulation(days, meeting_probability, patient_zero_health):
    # loading the patient function with the given health
    # setting first patient's health with the given value and rest patient's
    # health to 75.
    patient_simulation = load_patients(patient_zero_health)
    for i in range(len(patient_simulation)):
        if (i == 0):
            patient_simulation[i].set_health(patient_zero_health)
        else:
            patient_simulation[i].set_health(75)

    no_of_patients = []

    # to iterate through number of days
    for day in range(days):
        count = 0

        # retrive through the patient's object list
        for temp in patient_simulation:

            # Get the patient's connection
            frnds_list = temp.get_friends()

            # Iterating through each friend.
            for frnd in frnds_list:

                # Getting the random probabilty
                meet_prob = random.random()

                # Checking if the person is contagious
                if (meet_prob <= meeting_probability):
                    # If the random probability is less than the meeting probability
                    # then passing the viral load

                    if (temp.is_contagious()):
                        # calculating the viral load to set to new health.
                        viral_i = 5 + ((temp.get_health() - 25) ** 2 / 62)

                        # setting new health for the patient's friend based
                        # on the viral load.
                        frnd.infect(viral_i)

                # Getting the random probabilty
                meet_prob1 = random.random()
                # If the random probability is less than the meeting probability
                # then passing the viral load
                if (meet_prob1 <= meeting_probability):

                    # If the friend is contagious, then the patient is infected
                    # with the viral load.

                    if (frnd.is_contagious()):
                        # calculating the viral load to set to new health.
                        viral_j = 5 + ((frnd.get_health() - 25) ** 2 / 62)

                        # setting new health for the patient based
                        # on the viral load.
                        temp.infect(viral_j)

        # By the end of the day, chekcing for the number of contagious patients
        # and appending it to the list and making the patient sleep.
        for check_cont in patient_simulation:
            if (check_cont.is_contagious()):
                count = count + 1
            check_cont.sleep()
        no_of_patients.append(count)

    # Return the number of contagious patients for the given no of days.
    return no_of_patients


if __name__ == '__main__':
    # You may add your own testing code within this main block
    # to check if the code is working the way you expect.

    # This is a sample test case. Write your own testing code here.

    #  test_result = run_simulation(15, 0.8, 49)
    # print(test_result)

    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    #
    # Note: since this simulation is based on random probability, the
    # actual numbers may be different each time you run the simulation.

    #  test_result = run_simulation(30,0.5,30)
    #    print(test_result)

    # Another sample test case (high meeting probability means this will
    # spread to everyone very quickly; 40 days means will get 40 entries.)
    test_result = run_simulation(40, 1, 1)
    print(test_result)
    # sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

# do not add code here (outside the main block).
