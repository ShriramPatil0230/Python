class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getStatus(self):
        print(f"Name of train: {self.name}")
        print(f"Seats Awailable in train: {self.seats}")    

    def farInfo(self):
        print(f"Fare of Train is: Rs{self.fare}")

    def ticketBooking(self):
        if self.seats >= 1:
            print(f"Your seat is Booked:{self.seats}")
            self.seats= self.seats - 1
        else:
            print("Seats Not Awailable")

inf =Train("Train Rajdhani:246", 400, 90)
inf.getStatus()
inf.farInfo()
inf.ticketBooking()
inf.ticketBooking()
inf.ticketBooking()
inf.getStatus()