from rider import Rider
from cab import Cab
import time

class GoAnyWhere():

    def __init__(self):
        self.riders = {}
        self.cabs = {}
        self.bookings = {}
        self.currentUser = None
        self.autoGenrateCabs = False

    # define the countdown func.
    def countdown(self,t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("         Please wait...  :"+timer, end="\r")
            time.sleep(1)
            t -= 1
        
    def addCab(self,name,mobile,carnumber):
        cabObject= Cab(name,mobile,carnumber)
        if carnumber not in self.cabs:
            self.cabs[carnumber] = cabObject
        else:
            print("ERROR : Cab with same carnumber already exist.")

    def deleteCab(self, carnumber):
        if carnumber in self.cabs:
            self.cabs.pop(carnumber)
            print("cab deleted successfully")
            self.countdown(3)
        else:
            print("ERROR : Cab with carnumber not found.")

    def updateCabLocation(self,carnumber,x,y):
        if carnumber in self.cabs:
            cab = self.cabs[carnumber]
            cab.updateLocation(x,y)
            self.countdown(3)
        else:
            print("ERROR : Cab not found.")

    def showAllCabs(self):
        if self.autoGenrateCabs is False:
            self.addCab("abc","1234567890","cab1")
            self.addCab("Faiz","1234567891","cab2")
            self.addCab("Dex","1234567893","cab3")
            self.addCab("Smith","9876543210","cab4")
            self.addCab("John","1234569870","cab5")
            self.autoGenrateCabs = True
        print("Name   Driver's Number   Car Number")
        for key,value in self.cabs.items():
            print(value.name+"      "+value.mobile+"      "+key)

    #*************************************************************************************************************************************************

    def addRiders(self,name,mobile,password):
        riders = Rider(name,mobile,password)
        if mobile not in self.riders:
            self.riders[mobile] = riders
            print("Sign Up successfully!")
            self.countdown(3)
        else:
            print("ERROR : Rider with same mobile number already exists.")

    def deleteRiders(self,mobile,):
        if mobile in self.riders:
            self.riders.pop(mobile)
            print("Rider deleted successfully.")
        else:
            print("ERROR : Mobile Number not found.")

    def updateRidersLocation(self,mobile,x,y):
        if mobile in self.riders:
            riders = self.riders[mobile]
            riders.updateLocation(x,y)
            print("location updated.")
            self.countdown(3)
        else:
            print("ERROR : Location not found.")

    def riderPart(self):
        i=1
        while i!=0:
            self.showAllCabs()
            print("press 0 to log out")
            inp = input("Enter Cab number to book cab : ")
            if inp == 0:
                self.logOut()
                break
            elif inp in self.cabs:
                print(f"{self.cabs[inp]} booked successfully")
            elif inp not in self.cabs:
                print("Did not find any cab with this cab number Please try again.")
            else:
                 print("ERROR - Unsupported instruction")
            i = i+1

    def signUp(self,name,mobile,password):
        riders = Rider(name,mobile,password)
        if mobile not in self.riders:
            self.riders[mobile] = riders
            self.currentUser = riders
            print("signUp Successfully")
            self.countdown(3)
            self.riderPart()
        else:
            print("ERROR - username with same id already exists")
    
    def logIn(self, mobile, password):
        if mobile not in self.riders:
            print("Please signup")
            self.countdown(3)
        else:
            user = self.riders[mobile]
            if user.password == password:
                self.currentUser = user
                print("login successfully, Welcome {}!".format(user.name))
                self.countdown(3)
                self.riderPart()
            else:
                print("password is not matching!")
    
    def logOut(self):
        print("Logout successful, Good Bye {}".format(self.currentUser.name))
        self.currentUser = None
        self.countdown(3)

#start app
def main():
    i =1
    app = GoAnyWhere()

    def driver():
        while i!=0:
            print("Choose Options (1/2/3/0): ")
            print("1) Add Cab.")
            print("2) Delete Cab.")
            print("3) update Cab location.")
            print("for exit please type 0")
            inp = int(input("Enter Option : "))

            if inp == 1:
                name = input("Enter the driver name: ")
                mobile = input("Enter the driver's Mobile Number: ")
                carnumber = input("Enter the Car Number: ")
                app.addCab(name,mobile,carnumber)
            elif inp == 2:
                carNumber = input("Enter the driver's car number to be deleted : ")
                app.deleteCab(carNumber)
            elif inp == 3:
                carnumber = input("Enter Cab number: ")
                x = input("Enter position x : ")
                y = input("Enter position y : ")
                app.updateCabLocation(carnumber, x, y)
            elif inp == 0:
                break
            else:
                print("ERROR - Unsupported instruction")

    def rider():
        while i!=0:
            print("Choose Options (1/2/3/0): ")
            print("1) Sign Up.")
            print("2) Login.")
            print("for exit please type 0")
            inp = input("Enter Options : ")
            if inp == '1':
                name = input("Enter your full name : ")
                mobile = input("Enter your mobile number : ")
                password = input("Enter your password : ")
                app.signUp(name,mobile,password)
            elif inp == '2':
                mobile = input("Enter your mobile number : ")
                password = input("Enter your password : ")
                app.logIn(mobile,password)
            elif inp == '3':
                exit()
            else:
                print("ERROR - Unsupported instruction")


    while i!=0:
        print("Choose Options (1/2/3/0): ")
        print("1) If Driver.")
        print("2) If Rider.")
        print("for exit please type 0")
        inp = input("Enter Options : ")
        if inp == '1':
            driver()
        elif inp == '2':
            rider()
        elif inp == '0':
            exit()
        else:
            print("ERROR - Unsupported instruction")

    
#for start application
if __name__ == '__main__':
    main()