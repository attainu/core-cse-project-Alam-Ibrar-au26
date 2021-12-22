# CAB BOOKING

This project is intended to booking a cab. It's written in python and offers all functionalities through instruction set given via command line.

## Requirements

register a rider to book a can on GoAnyWhere.

### Modules Used

I have used two modules which is mentioned below:
import time(this is used for day,time & date formate)
import uuid(it is used to generate random/unique id)
pickle

### Approach Used

This project is based on OOP'S concept

    Main(class): In this class we have implemented different functionalities like on board countdown, addcab, deletecab, updatecablocation, showallcabs, addriders, deleteriders, updateriderslocation, rider part, signup, login, logout etc. 

    Bookings(class): In this class we have implemented different functionalities like modifying quantity etc.

    Riders(class): In this class is created to riders details like display details, update location and get location.

    cab(class): In this class is created to cabs details like display details, update location and get location.


#### Instruction to run

This program are driven based on instruction set. It accepts number of test cases as first input and then ready that many times to get instruction from command line. It performs operations based on given instruction and print result on screen.