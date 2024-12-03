# Contractor UI Logic
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
  {BLUE}
          _____                    _____                    _____                            _____                    _____                    _____          
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
{RED}
                                                           ------------------
                                                          |Welcome to NAN AIR|
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
| Please select a role:                                                                                                                                       |
| 1. manager                                                                                                                                                  |
| 2. employee                                                                                                                                                 |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                              """

print(main_menu_1)

employee_main_menu = f"""
{RED}
                                                           ----------
                                                          |Main menue|
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
| 1. view location                                                                                                                                            |
| 2. view properties                                                                                                                                          |
| 3. view employees                                                                                                                                           |
| 4. view contractors                                                                                                                                         |
| 5. view managers                                                                                                                                            |
| 6. view active tasks  	                                                                                                                              |
| 7. make a report                                                                                                                                            |
| b. back 	                                                                                                                                              |
| q. quit                                                                                                    	                                              |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                              """

print(employee_main_menu)

# input 1 (displays 6 locations)

employee_view_location = f"""
{RED}
                                                           ------------------
                                                          |Viewing locations|
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
| 1. Reykjavík                                                                                                                                                |
| 2. Nuuk                                                                                                                                                     |
| 3. Kulusuk                                                                                                                                                  |
| 4. Þórshöfn                                                                                                                                                 |
| 5. Tingwall                                                                                                                                                 |
| 6. Longyearbyen                                                                                                                                             |
| b. back                                                                                                                                                     |
| q. quit                                                                                                      	                                              |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                              """
print(employee_view_location)
# input 1

employee_view_reykjavik = f"""
{RED}
                                                           -------------------------------
                                                          |Viewing properties in Reykjavik|
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
| 1. view property by ID                                                                                                                                      |
| b. back                                                                                                                                                     | 
| q. quit                                                                                                                                                     |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                              """
print(employee_view_reykjavik)
#input 1

# Enter a property ID: (Sample F12345)
viewing_property_by_ID = f"""
{RED}
                                                           ----------------
                                                          |Viewing property|
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
| 1. View employees                                                                                                                                           |
| 2. View manager                                                                                                                                             |
| 3. View contractors                                                                                                                                         |
| 4. View maintenance tasks                                                                                                                                   |
| b. back                                                                                                                                                     | 
| q. quit                                                                                                                                                     |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                              """
print(viewing_property_by_ID)
# input b
# input b
# input b
# input 2 to view all properties

employee_view_all_properties  = f"""
{RED}
                                                           -----------------------
                                                          |Viewing all properties |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
| 1. view property by ID                                                                                                                                      |
| b. back                                                                                                                                                     | 
| q. quit                                                                                                                                                     |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                              """
print(employee_view_all_properties)
# input b
# input 3 in main menue

employee_view_all_employees = f"""
{RED}
                                                           ----------------------
                                                          |Viewing all employees |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
| 1. view emplyees by ID                                                                                                                                      |
| b. back                                                                                                                                                     | 
| q. quit                                                                                                                                                     |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                              """
print(employee_view_all_employees)
# input b 
# input 4 in main menue

employee_view_all_contractors = f"""
{RED}
                                                           ------------------------
                                                          |Viewing all contractors |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
| 1. view contractors by ID                                                                                                                                   |
| b. back                                                                                                                                                     | 
| q. quit                                                                                                                                                     |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                              """
print(employee_view_all_contractors)
# input b
# input 5 in main menue

employee_view_all_managers = f"""
{RED}
                                                           ---------------------
                                                          |Viewing all managers |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
| 1. view managers by ID                                                                                                                                      |
| b. back                                                                                                                                                     | 
| q. quit                                                                                                                                                     |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                              """
print(employee_view_all_managers)
# input b
# input 6 in main menue

employee_view_active_tasks = f"""
{RED}
                                                           -------------------------
                                                          |Viewing all active tasks |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
| b. back                                                                                                                                                     |
| q. quit                                                                                                                                                     |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                              """
print(employee_view_active_tasks)
#input b
# input 7 in main menue

employee_make_a_report = f"""
{RED}
                                                           --------------
                                                          |Make a report |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
| 1. Enter employee ID                                                                                                                                        |
| 2. Enter date and time                                                                                                                                      |
| 3. refer a contractor                                                                                                                                       |
| 4. write a report                                                                                                                                           |
| 5. is the task complete? Y/N                                                                                                                                |
| 6. Turn in report                                                                                                                                           |
| b. back                                                                                                                                                     |
| q. quit                                                                                                                                                     |
 -------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                              """
print(employee_make_a_report)
# input b
# input 8 in main menue


# def defaultScreen(params):
#     [title, 1, 2,3,4,5,6]
#     spacenum = 160
#     count_params = params.size() - 1
#     print(spacenum * "-")
#     for index,param in enumerate(params[1:]):
#         default_param_print = f"| {index+1}. {param} {" " * spacenum - len(param)} |"

#     print(spacenum * "-")
#     employee_make_a_report = f"""
# {RED}
#                                                            --------------
#                                                     |{params[0]} |
#  -------------------------------------------------------------------------------------------------------------------------------------------------------------
# | 1.                  {param2}                                                                                                      |
# | 2. Enter date and time                                                                                                                                      |
# | 3. refer a contractor                                                                                                                                       |
# | 4. write a report                                                                                                                                           |
# | 5. is the task complete? Y/N                                                                                                                                |
# | 6. Turn in report                                                                                                                                           |
# | b. back                                                                                                                                                     |
# | q. quit                                                                                                                                                     |
#  -------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                                                                                               """
