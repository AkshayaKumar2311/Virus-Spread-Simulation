"""
# PYTHON TASK 1
# Assignment 2 - FIT9136
# Student ID : 31021301
# Created on Fri May 22 2020
# Author: Akshaya Kumar Chandrasekaran / Co_Author : Namrata Palai
# Last modified : 04-06-2020
#
#In this py file,  a person class and objects for the class is created
#for establising connections for the objects.
#This py file has Person class with methods constructor,add_friend(),
#get_name(),get_friends(),get_friends_name()
#and a function load_people()
"""


# Creating person class and defining methods

class Person:

    # Creating constructor that takes person's first name and last name
    # as input

    # Creating a list object to save the connection for the person

    # Dictionary is used to add a friend for a person object
    # Here key is the main person and value is a list of person objects
    # (their connection)
    # Since it is clearly mentioned that only unique name is selected as friends
    # check for friend already exists as a connection is done. If they exists
    # then the friend object is not added . If there is no connection, then
    # the friend object is added as connection to the main person.

    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.name = self.fname + " " + self.lname
        self.dict = {}
        self.frnds_list = []

    # add_friend takes the person object and appends to the person's list
    # per the connection given
    def add_friend(self, friend_person):
        self.dict[self.name] = self.frnds_list
        check_friends = self.get_friends()
        if (friend_person not in check_friends):
            self.frnds_list.append(friend_person)
            self.dict[self.name] = self.frnds_list

    # Returns the name of the person object called
    def get_name(self):
        return self.name

    # Returns the person object as list (Friends list for the person is
    # returned as list of person objects)
    def get_friends(self):
        return self.dict[self.name]

    # Returns the connections name as list (Friends list for the person is
    # returned as LIST OF STRING NAMES)
    def get_friends_name(self):
        friend_names = []
        for frnd in self.frnds_list:
            friend_names.append(frnd.get_name())
        return friend_names


# load_people is a function that reads data from the text file given and
# saves it as a list

# Once all the split based on the delimiter is done, A person object is created
# for all the unique name mentioned.

# Once person object for all the unique name is created, add_friend function is
# called and the connection is established by adding friends.


def load_people():
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

    # To create person object and to store the same, from the unique name list,
    # first name and last name is split and passed in as two arguments as fname
    # and lname and creating person object.

    # These objects will get saved exactly in the index as that of the unique
    # name, so that values can be compared easily and correct object is added

    person_obj = []
    for i in range(len(unique_name)):
        fname, lname = unique_name[i].split()
        person_obj.insert(i, Person(fname, lname))

    # For the length of the friend list,
    for i in range(len(frnds_list)):

        # for the length of each friend a person has
        for j in range(len(frnds_list[i])):

            # to iterate through the unique name to get the index of the
            # person we are looking for
            for temp in range(len(unique_name)):
                # only if the person we are looking for matches with the
                # unique name, add that person object as a friend of person
                if (unique_name[temp] == frnds_list[i][j]):
                    person_obj[i].add_friend(person_obj[temp])

    # returns the list of person object
    return person_obj


if __name__ == '__main__':
    check_people = load_people()
    check125 = (check_people[125].get_friends())
    check0 = (check_people[0].get_friends())
    check0_names = (check_people[0].get_friends_name())
    check26 = (check_people[26].get_friends())
    check0[2] == check26[4]
    print(check_people[1].get_name())
    print(check_people[125].get_name())
    check1 = (check_people[1].get_friends())
    check1_names = (check_people[1].get_friends_name())
    check10 = (check_people[10].get_friends())
    check10_names = (check_people[10].get_friends_name())

    print(check1, check1_names)
    print(check10, check10_names)

# do not add code here (outside the main block).
