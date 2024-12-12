#from Logic_Layer import LogicLayerAPI

class ContractorUILogic:
    def __init__(self):
        pass

RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

banner = f"""
  {BLUE}          _____                    _____                    _____                            _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                          /\    \                  /\    \                  /\    \         
        /::\____\                /::\    \                /::\____\                        /::\    \                /::\    \                /::\    \        
       /::::|   |               /::::\    \              /::::|   |                       /::::\    \               \:::\    \              /::::\    \       
      /:::::|   |              /::::::\    \            /:::::|   |                      /::::::\    \               \:::\    \            /::::::\    \      
     /::::::|   |             /:::/\:::\    \          /::::::|   |                     /:::/\:::\    \               \:::\    \          /:::/\:::\    \     
    /:::/|::|   |            /:::/__\:::\    \        /:::/|::|   |                    /:::/__\:::\    \               \:::\    \        /:::/__\:::\    \    
   /:::/ |::|   |           /::::\   \:::\    \      /:::/ |::|   |                   /::::\   \:::\    \              /::::\    \      /::::\   \:::\    \   
  /:::/  |::|   | _____    /::::::\   \:::\    \    /:::/  |::|   | _____            /::::::\   \:::\    \    ____    /::::::\    \    /::::::\   \:::\    \  
 /:::/   |::|   |/\    \  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \          /:::/\:::\   \:::\    \  /\   \  /:::/\:::\    \  /:::/\:::\   \:::\____\ 
/:: /    |::|   /::\____\/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\        /:::/  \:::\   \:::\____\/::\   \/:::/  \:::\____\/:::/  \:::\   \:::|    |
\::/    /|::|  /:::/    /\::/    \:::\  /:::/    /\::/    /|::|  /:::/    /        \::/    \:::\  /:::/    /\:::\  /:::/    \::/    /\::/   |::::\  /:::|____|
 \/____/ |::| /:::/    /  \/____/ \:::\/:::/    /  \/____/ |::| /:::/    /          \/____/ \:::\/:::/    /  \:::\/:::/    / \/____/  \/____|:::::\/:::/    / 
         |::|/:::/    /            \::::::/    /           |::|/:::/    /                    \::::::/    /    \::::::/    /                 |:::::::::/    /  
         |::::::/    /              \::::/    /            |::::::/    /                      \::::/    /      \::::/____/                  |::|\::::/    /   
         |:::::/    /               /:::/    /             |:::::/    /                       /:::/    /        \:::\    \                  |::| \::/____/    
         |::::/    /               /:::/    /              |::::/    /                       /:::/    /          \:::\    \                 |::|  ~|          
         /:::/    /               /:::/    /               /:::/    /                       /:::/    /            \:::\    \                |::|   |          
        /:::/    /               /:::/    /               /:::/    /                       /:::/    /              \:::\____\               \::|   |          
        \::/    /                \::/    /                \::/    /                        \::/    /                \::/    /                \:|   |          
         \/____/                  \/____/                  \/____/                          \/____/                  \/____/                  \|___|          
                                                                                                                                                              """

print(banner)

def main_menu():
    while True:  # Loop until a valid choice is made
        try:
            main_menu_select_role = input(f"""
{RED}                                                           ------------------
                                                          |Welcome to NAN AIR|
------------------------------------------------------------------------------------------------------------------------------------------------
| Please select a role:                                                                                                                         |
| 1. Manager                                                                                                                                    |
| 2. Employee                                                                                                                                   |
-------------------------------------------------------------------------------------------------------------------------------------------------
| INPUT: """)
            if main_menu_select_role == '1':
                manager_main_menu() #call the manager menu function
            elif main_menu_select_role == '2':
                print("Employee option selected. This feature is not implemented yet.")
                break
            else:
                print("Invalid selection. Please select 1 for Manager or 2 for Employee.")
        except ValueError:
            print("Please enter a valid number.")

#Input 1
def manager_main_menu():
    while True:
        try:            
            menu_choice = input (f"""
{RED}                                                           ------------------
                                                          |Welcome to NAN AIR|
----------------------------------------------
| Hello, Manager. What would you like to do? |
| 1. Employees Database                      |
| 2. Contractors Database                    |
| 3. Destinations Database                   |
| 4. Reports Database                        |
| B. Back                                    |
| Q. Quit                                    |                                                                                              
------------------------------------------------------------------------------------------------------------------------------------------------- 
| INPUT: """)
            if menu_choice == '1':
                manager_main_menu_employees()
            elif menu_choice == '2':
                manager_main_menu_contractors()
            elif menu_choice == '3':
                manager_main_menu_destinations()
            elif menu_choice == 'B' or menu_choice == 'b':
                return
            elif menu_choice == 'Q' or menu_choice == 'q':
                print("Exiting program. Goodbye!")
                exit()
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number.")
            

#MAIN MENU Input 1: Employees Databa
def manager_main_menu_employees():
    while True:
        try:
            menu_choice = input(f"""
{RED}                                                           ------------------
                                                          |Employees Database|
--------------------------------------
| Employee Database for NAN Airlines |
| 1. View Employees                  |
| 2. Edit Employee Data              |
| 3. Add Employee                    |
| 4. Delete Employee Data            |
| B. Back                            |
| Q. Quit                            |
------------------------------------------------------------------------------------------------------------------------------------------------
| INPUT: """)
            if menu_choice == '1':
                manager_main_menu_employees_list()
            elif menu_choice == '2':
                manager_main_menu_employees_edit()
            elif menu_choice == 'B' or menu_choice == 'b':
                return
            elif menu_choice == '3':
                manager_main_menu_employees_add()
            elif menu_choice == '4':
                pass
            else:
                print("Invalid selection. Please try again...")
        except ValueError:
            print("Please enter a valid selection.")


#Employees Database INPUT 1 
def manager_main_menu_employees_list():
        while True:
            try:
                menu_choice = input(f"""
{RED}                                                           ------------------
                                                          |Viewing Employees|

------------------------------------------------------------------------------------------------------------------------------------------------
|   ID  |             NAME            |   LOCATION     | SOCIAL SECURITY NUMBER |   PHONE    |   MOBILE PHONE    |          EMAIL |             |
------------------------------------------------------------------------------------------------------------------------------------------------
| 61330 |   Olafur Hafstein           |    Reykjavik   |     ****** - ****      | 555 - 5555 |  888 - 8888       |  olafurv10@gmail.com         |
| 33016 |   Grimur Dagur Grimsson     |      Nuuk      |     ****** - ****      | 555 - 5555 |  888 - 8888       |  GrimurD@gmail.com           |
| 30361 |   Iðunn Maria Gunnarsdottir |    Kulusuk     |     ****** - ****      | 555 - 5555 |  888 - 8888       |  IdunnMG@gmail.com           |
| 03316 |   Mani Elvar Traustason     |    Tingwall    |     ****** - ****      | 555 - 5555 |  888 - 8888       |  ManiET@gmail.com            |
|------------------------------------------------------------------------------------------------------------------------------------------------
| B. Back                                                                                                                                       |
| Q. Quit                                                                                                                                       |
------------------------------------------------------------------------------------------------------------------------------------------------- 
| INPUT: """)
                if menu_choice == '1':
                    pass
                if menu_choice == 'B' or menu_choice == 'b':
                    return
            except ValueError:
                print("Please enter a valid selection.")
#Employees Database INPUT 2
def manager_main_menu_employees_edit():
        while True:
            try:
                menu_choice = input(f"""
{RED}                                                           ------------------
                                                          |Employees Database|
-----------------------------------------------------------------------------------------------------------------------------------------------
| To edit data from NaN Airlines Employee, please put in Employe ID Number:                                                                   |
| Press ESC to go back.                                                                                                                       |
-----------------------------------------------------------------------------------------------------------------------------------------------
| INPUT: """)
                if menu_choice == 'esc':
                    return    
            except ValueError:
                    print("Please input numbers only.")
#Employees Databa INPUT 2
manager_main_menu_employees_edit = f"""
{RED}                                                           ------------------
                                                          |Employees Database|
---------------------------------------------------------------------------------------------------------------------------------------------
|   ID  |             NAME            |   LOCATION     | SOCIAL SECURITY NUMBER |   PHONE    |   MOBILE PHONE    |          EMAIL           |  
---------------------------------------------------------------------------------------------------------------------------------------------
| 61330 |   Olafur Hafstein           |    Reykjavik   |     ****** - ****      | 555 - 5555 |  888 - 8888       |  olafurv10@gmail.com     |
--------------------------------------------------------------------------------------------------------------------------------------------|
INPUT:ID 03361 
--------------------------------------------------------------------------------------------------------------------------------------------- """

#Employees Databa INPUT 3
def manager_main_menu_employees_add():
        while True:
            try:
                menu_choice = input(f"""
{RED}                                                           ------------------
                                                          |Add Employee|
---------------------------------------------------------------------------------------------------------------------------------------------
|   ID  |             NAME            |   LOCATION     | SOCIAL SECURITY NUMBER |   PHONE    |   MOBILE PHONE    |          EMAIL           | 
---------------------------------------------------------------------------------------------------------------------------------------------
|       |                             |                |                        |            |                   |                          | 
--------------------------------------------------------------------------------------------------------------------------------------------|
| /back = Go Back
| /quit = Quit
| /id = Input ID
| /name = Input employee name
| /location = Input Employee's location of work
| /snumber = Input Social Security Number
| /phone = Input employee's home number
| /mphone = Input Employee's mobile number
| /email = Input Employee's email
--------------------------------------------------------------------------------------------------------------------------------------------|
|ID: """)
                if menu_choice == '/back':
                    return
                elif menu_choice == '/quit':
                    break
            except ValueError:
                print("Invalid input. Please try again...")

#Employees Database INPUT 4 
manager_main_menu_employees_delete = f"""
{RED}                                                           ------------------
                                                          |Viewing Employees|

------------------------------------------------------------------------------------------------------------------------------------------------
|   ID  |             NAME            |   LOCATION     | SOCIAL SECURITY NUMBER |   PHONE    |   MOBILE PHONE    |          EMAIL |             |
------------------------------------------------------------------------------------------------------------------------------------------------
| 61330 |   Olafur Hafstein           |    Reykjavik   |     ****** - ****      | 555 - 5555 |  888 - 8888       |  olafurv10@gmail.com         |
| 33016 |   Grimur Dagur Grimsson     |      Nuuk      |     ****** - ****      | 555 - 5555 |  888 - 8888       |  GrimurD@gmail.com           |
| 30361 |   Iðunn Maria Gunnarsdottir |    Kulusuk     |     ****** - ****      | 555 - 5555 |  888 - 8888       |  IdunnMG@gmail.com           |
| 03316 |   Mani Elvar Traustason     |    Tingwall    |     ****** - ****      | 555 - 5555 |  888 - 8888       |  ManiET@gmail.com            |
|-----------------------------------------------------------------------------------------------------------------------------------------------|
| B. Back                                                                                                                                       |
| Q. Quit                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------|
|Please Input Employee's ID Number: 61330                                                                                                       |
------------------------------------------------------------------------------------------------------------------------------------------------- """

manager_main_menu_employees_delete = f"""
{RED}                                                           ------------------
                                                          |Employees Database|
---------------------------------------------------------------------------------------------------------------------------------------------
|   ID  |             NAME            |   LOCATION     | SOCIAL SECURITY NUMBER |   PHONE    |   MOBILE PHONE    |          EMAIL           | 
---------------------------------------------------------------------------------------------------------------------------------------------
| 61330 |   Olafur Hafstein           |    Reykjavik   |     ****** - ****      | 555 - 5555 |  888 - 8888       |  olafurv10@gmail.com     |
---------------------------------------------------------------------------------------------------------------------------------------------
| /delete = Delete information
| B. Back
| Q. Quit
--------------------------------------------------------------------------------------------------------------------------------------------|
|INPUT: /delete 
|WARNING: You are about to delete ALL information on Employee #61330. This CANNOT be undone. Please write 'YES' to confirm or 'NO' to cancel.
|INPUT:....
--------------------------------------------------------------------------------------------------------------------------------------------- """


#MAIN MENU Input 2: Contractors Database
def manager_main_menu_contractors():
    while True:
        try:
            menu_choice = input(f"""
{RED}                                                           ------------------
                                                          |Contractors Database|
---------------------------------------------------------------------------------------------------------------------------------------------
| Please select a role:                                                                                                                     |
| 1. Contractor Contacts                                                                                                                    |
| 2. Request Maintenance                                                                                                                    |
| 3. Check Maintenance Reports                                                                                                              |
| B. Back                                                                                                                                   |
| Q. Quit                                                                                                                                   |
--------------------------------------------------------------------------------------------------------------------------------------------- 
| INPUT: """)
            if menu_choice == '1':
                    manager_main_menu_contractors_contacts()
            elif menu_choice == 'b':
                return
            elif menu_choice == '3':
                    manager_main_menu_contractors_request_maintenance_reports()
        except ValueError:
            print("Please input valid option.")

#Contractors Database: INPUT 1
def manager_main_menu_contractors_contacts():
    while True:
        try:
            menu_choice = input(f"""
{RED}                                                     ---------------------
                                                          |Contractor Database|
|-----------------------------------------------------------------------------------------------------------------|
|           NAME            |   LOCATION     | SOCIAL SECURITY NUMBER |      PHONE     |          EMAIL           |
|-----------------------------------------------------------------------------------------------------------------|
|      Hús og Við ehf.      |   Reykjavik    |     ****** - ****      |   766 - 6777   |    hus ogvid@husogvid.is | 
|-----------------------------------------------------------------------------------------------------------------|
|   Blue Water Shipping     |   Greenland    |     ****** - ****      | +299 325 - 410 |        nuuk@bws.net      |
|-----------------------------------------------------------------------------------------------------------------|
| /add = Add Contractor                                                                                           |
| /edit = Edit Contractor information                                                                             |
| /delete = Delete Contractor information                                                                         |
| B. Back                                                                                                         |
| Q. Quit                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------|
|INPUT: """)
            if menu_choice == 'B' or menu_choice == 'b':
                return
        except ValueError:
            print("Please input valid option.")

#Contractors Database: INPUT 1
def manager_main_menu_contractors_request_maintenance_contractors():
    while True:
        try:
            menu_choice = input(f"""
{RED}                                                     ---------------------
                                                          |Contractor Database|
|---------------------------------------------------------------------------------------------------------------------------|
|     #   |           NAME            |   LOCATION     | SOCIAL SECURITY NUMBER |      PHONE     |          EMAIL           |
|---------------------------------------------------------------------------------------------------------------------------|
|     1   |     Hús og Við ehf.       |   Reykjavik    |     ****** - ****      |   766 - 6777   |    hus ogvid@husogvid.is | 
|---------------------------------------------------------------------------------------------------------------------------|
|     2   |    Blue Water Shipping    |   Greenland    |     ****** - ****      | +299 325 - 410 |        nuuk@bws.net      |                                   
|---------------------------------------------------------------------------------------------------------------------------|
| /# | /EMAIL = To insert email to selected Contractor                                                                      |
| B. Back                                                                                                                   |
| Q. Quit                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------|
 INPUT: """)
            if menu_choice == 'B' or menu_choice == 'b':
                return
        except ValueError:
                print("Please input valid option.")

#Contractors Databa: INPUT 2
def manager_main_menu_contractors_request_maintenance_locations():
    while True:
        try:
            menu_choice = input(f"""
{RED}                                                     ----------------------
                                                          |Contractors Database|
|------------------------------------------------------------------------|
|   #   |        ADDRESS        |   LOCATION     | LAST MAINTENANCE CHECK|
|------------------------------------------------------------------------|
|   1   |  30 Nalunaq, Avannaa  |   Greenland    |      02/11/2024       |
|------------------------------------------------------------------------|
| /# = Selects Housing for maintenance check                             |   
| B. Back                                                                |
| Q. Quit                                                                |
|------------------------------------------------------------------------|
 INPUT: """)
            if menu_choice == 'B' or menu_choice == 'b':
                return
        except ValueError:
            print("Please input valid option.")

#Contractors Database: INPUT 3
def manager_main_menu_contractors_request_maintenance_reports():
    while True:
        try:
            menu_choice = input(f"""
{RED}                                                     ---------------------
                                                          |Contractor Database|
|----------------------------------------------------------------------|
|     #   |           FROM            |    ADDRESS      |      DATE    |
|----------------------------------------------------------------------|
|     1   |     Hús og Við ehf.       |    Reykjavik    |  01/06/2024  |                                                                                                                           
|----------------------------------------------------------------------|
|     2   |    Blue Water Shipping    |    Greenland    |  02/08/2024  |
|----------------------------------------------------------------------|
| /# = To select and open Maintenance Report File                      |
| B. Back                                                              |
| Q. Quit                                                              |
|----------------------------------------------------------------------|
 INPUT: """)
            if menu_choice == 'B' or menu_choice == 'b':
                return
        except ValueError:
            print("Please input valid option...")

#MAIN MENU Input 3: Destinations Database
def manager_main_menu_destinations():
    while True:
        try:
            menu_choice = input(f"""
{RED}                                                           ------------------
                                                          |Destinations Database|
-------------------------------------------------------------------------------------------------------------------------------------
| Please select a role:                                                                                                              |
| 1. View Destinations                                                                                                               |
| 2. Edit Destinations                                                                                                               |
| 3. Add Destinations                                                                                                                |
| 4. Remove Destination                                                                                                              |
| B. Back                                                                                                                            |
| Q. Quit                                                                                                                            |
-------------------------------------------------------------------------------------------------------------------------------------
 INPUT: """)
            if menu_choice == '1':
                manager_main_menu_destinations_view()
            elif menu_choice == '2':
                manager_main_menu_destinations_edit()
            elif menu_choice == 'B' or menu_choice == 'b':
                return
        except ValueError:
            print("Please input valid option...")


#Destinations Database INPUT 1: View Destinations
def manager_main_menu_destinations_view():
    while True:
        try:
            menu_choice = input(f"""
{RED}                                                           ------------------
                                                          |Destinations Database|
-------------------------------------------------------------------------------------------------------------------------------------
|   Airport ID  |   Country     |   Airport     |   Flight Time |   Distance    |   Manager     | Manager Phone |   Manager Email   | 
|-----------------------------------------------------------------------------------------------------------------------------------| 
|               |               |               |               |               |               |               |                   |
|-----------------------------------------------------------------------------------------------------------------------------------|
| B. Back                                                                                                                           |
| Q. Quit                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------|
 INPUT: """)
            if menu_choice == 'B' or menu_choice == 'b':
                return
            elif menu_choice == 'Q' or menu_choice == 'q':
                break
        except ValueError:
            print("Please input Valid option...")

#Destinations Database INPUT 2 Edit Destinations
def manager_main_menu_destinations_edit():
    while True:
        try:
            menu_choice = input(f"""
{RED}                                                           ------------------
                                                          |Destinations Database|
-------------------------------------------------------------------------------------------------------------------------------------
|   Airport ID  |   Country     |   Airport     |   Flight Time |   Distance    |   Manager     | Manager Phone |   Manager Email   | 
|-----------------------------------------------------------------------------------------------------------------------------------| 
|               |               |               |               |               |               |               |                   |
|-----------------------------------------------------------------------------------------------------------------------------------|
| /edit = Edit Destinations information                                                                                             |
| B. Back                                                                                                                           |
| Q. Quit                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------|
 INPUT: """)
            if menu_choice == 'B' or menu_choice == 'b':
                return
            elif menu_choice == 'Q' or menu_choice == 'q':
                break
        except ValueError:
            print("Please input valid option...")


##MAIN MENU Input 4: Reports Database+-
manager_main_menu_reports = f"""
{RED}                                                           ------------------
                                                          |Welcome to NAN AIR|
-------------------------------------------------------------------------------------------------------------------------------------
| Please select a role:                                                                                                             |
| 1. Employee Reports                                                                                                               |
| 2. Maintenance Reports                                                                                                            |
| 3. Customer Complaints                                                                                                            |
| B. Back                                                                                                                           |
| Q. Quit                                                                                                                           |
------------------------------------------------------------------------------------------------------------------------------------- """
#
main_menu()