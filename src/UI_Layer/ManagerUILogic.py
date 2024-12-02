from Logic_Layer import LogicLayerAPI

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

main_menu_1 = f"""
{RED}                                                           ------------------
                                                          |Welcome to NAN AIR|
------------------------------------------------------------------------------------------------------------------------------------------------
| Please select a role:                                                                                                                         |
| 1. manager                                                                                                                                    |
| 2. employee                                                                                                                                   |
-------------------------------------------------------------------------------------------------------------------------------------------------
 
                                                                                                                                                                                                                                                    """

print(main_menu_1)
#Input 1
manager_main_menu = f"""
{RED}                                                           ------------------
                                                          |Welcome to NAN AIR|
------------------------------------------------------------------------------------------------------------------------------------------------
| Please select a role:                                                                                                                         |
| 1. Employees Database                                                                                                                          
| 2. Contractors Database
| 3. Destinations Database
| 4. Reports Database
| B. Back
| Q. Quit                                                                                                                                  |
------------------------------------------------------------------------------------------------------------------------------------------------- """
#MAIN MENU Input 1: Employees Databa
manager_main_menu_employees = f"""
{RED}                                                           ------------------
                                                          |Welcome to NAN AIR|
------------------------------------------------------------------------------------------------------------------------------------------------
| Please select a role:                                                                                                                         |
| 1. View Employees                                                                                                                         
| 2. Edit Employee Data 
| 3. Add Employee
| 4. Delete Employee Data
| B. Back
| Q. Quit                                                                                                                                  |
------------------------------------------------------------------------------------------------------------------------------------------------- """
#Employees Databa
manager_main_menu_employees = f"""
{RED}                                                           ------------------
                                                          |Welcome to NAN AIR|
------------------------------------------------------------------------------------------------------------------------------------------------
| Please select a role:                                                                                                                         |
| 1. View Employees                                                                                                                         
| 2. Edit Employee Data 
| 3. Add Employee
| 4. Delete Employee Data
| B. Back
| Q. Quit                                                                                                                                  |
------------------------------------------------------------------------------------------------------------------------------------------------- """

#MAIN MENU Input 2: Contractors Database
manager_main_menu_contractors = f"""
{RED}                                                           ------------------
                                                          |Welcome to NAN AIR|
------------------------------------------------------------------------------------------------------------------------------------------------
| Please select a role:                                                                                                                         |
| 1. Contractor Contacts
| 2. Request Maintenance
| 3. Check Maintenance Reports
| B. Back
| Q. Quit                                                                                                                                  |
------------------------------------------------------------------------------------------------------------------------------------------------- """
#MAIN MENU Input 3: Destinations Database
manager_main_menu_destinations = f"""
{RED}                                                           ------------------
                                                          |Welcome to NAN AIR|
------------------------------------------------------------------------------------------------------------------------------------------------
| Please select a role:                                                                                                                         |
| 1. View Destinations                                                                                                                         
| 2. Edit Destinations 
| 3. Add Destinations
| 4. Remove Destination
| B. Back
| Q. Quit                                                                                                                                  |
------------------------------------------------------------------------------------------------------------------------------------------------- """

print(main_menu_1)
#MAIN MENU Input 4: Reports Database
manager_main_menu_reports = f"""
{RED}                                                           ------------------
                                                          |Welcome to NAN AIR|
------------------------------------------------------------------------------------------------------------------------------------------------
| Please select a role:                                                                                                                         |
| 1. Employee Reports                                                                                                                         
| 2. Maintenance Reports
| 3. Customer Complaints
| B. Back
| Q. Quit                                                                                                                                  |
------------------------------------------------------------------------------------------------------------------------------------------------- """

print(main_menu_1)