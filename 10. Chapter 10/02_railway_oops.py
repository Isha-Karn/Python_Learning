import pandas as pd

pd.DataFrame()

class RailwayForm:
    #formtype="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

ishaApplication= RailwayForm()
ishaApplication.name= "Isha"
ishaApplication.train= "Rajdhani express"
ishaApplication.printData()
