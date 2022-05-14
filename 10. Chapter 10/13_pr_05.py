class Train():
    def __init__(self, name, fare, seats):
        self.name= name
        self.seats= seats
        self.fare= fare

    def getStatus(self):
        print(f"Name of tarin: {self.name}")
        print(f"Number of seats available: {self.seats}")

    def fareInfo(self):
        print(f"The fare price is: {self.fare}")

    def bookTicket(self):
        if (self.seats>0):
            print(f"Your ticket has been booked. Your seat number is {self.seats}")
            self.seats= self.seats-1
        else:
            print("Sorry! the seat is not available")

a= Train("Rajdhani Express", 500, 2)
a.getStatus()
a.bookTicket()
a.bookTicket()
a.bookTicket()
a.fareInfo()
a.getStatus()




