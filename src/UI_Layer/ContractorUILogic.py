from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .ViewUILogic import ViewUILogic
from .Displays import Displays

class ContractorUILogic:
    def __init__(self):
        self.LogicLayerWrapper = LogicLayerAPI()
        self.ViewUI = ViewUILogic()

    def run(self):
        while True:
            print("1: To access viewing features")
            print("2: To access .... something with maintenance ....")
            print("B to go Back")
            print("Q to quit")
            user_choice = input("Choice ")
            # Exit out of the loop

            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            if user_choice.lower() == "b":
                print("Going back")
                break

            if user_choice == "1":
                self.ViewUI.viewMenu()
            elif user_choice == "2":
                pass
                #self.MAINTENANCE SOMETHING FUNCTION
            else:
                print("Invalid Input")
