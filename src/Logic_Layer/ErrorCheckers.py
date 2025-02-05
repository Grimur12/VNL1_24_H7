# Error checker class for all error checks
from datetime import datetime

class ErrorCheckers:

    def __init__(self) -> None:
        pass
    
    def checkNumber(self, input) -> True:
        """ Returns True if user input is a number, raises ValueError otherwise"""
        # Used for example to check both for input when changing information and as count.
        try:
            int(input)
        except ValueError: # Try to change it into integer if it cant we raise the error
            raise ValueError("Input must be a valid number")
        return True

    def checkEmpty(self, input) -> True:
        """ Returns True if user input is not empty, raises ValueError otherwise """
        # We cant have empty as an input
        if input == "":
            raise ValueError("Input can not be empty")
        return True

    def errorCheckName(self, name) -> True:
        """ Checks if name a number, if so raises ValueError, otherwise returns True"""
        self.checkEmpty(name) # Checks if the name is empty
        if name.isnumeric(): # Or if its numeric
            raise ValueError("Name must not be a number")
        return True
    
    def errorCheckDescription(self, input) -> True:
        """Checks if input is just or is bigger than 250 characters, returns ValueError or True"""
        self.checkEmpty(input)
        if input.isnumeric():
            raise ValueError("Description can not be just a number")
        elif len(input) > 250:
            raise ValueError("Description can not be more than 100 characters")
        else:
            return True

    def errorCheckAddress(self, address) -> True:
        """ Checks if Address user input is valid, if so returns True, if not raises ValueError """
        self.checkEmpty(address) # Checks if the address is empty
        if address.isnumeric(): # And makes sure that its actually a number inside the string
            raise ValueError("Address must not be just a number")
        return True

    def errorCheckSocialSecurity(self, socialSecurity) -> True:
        """ Checks if Social Security number user input is valid, if so returns True, if not raises ValueError """
        # Format we want is XXXXXX-XXXX
        self.checkEmpty(socialSecurity)
        if "-" in socialSecurity: # Checks if there is a - in the string
            social_split = socialSecurity.split("-") # Split it into the parts of the social we want should be 6 and 4
            if len(social_split[0]) == 6 and len(social_split[1]) == 4: # Checks if the split strings are of the correct length for the format
                if social_split[0].isnumeric() and social_split[1].isnumeric(): # And checks if they are for sure numbers
                    return True
                else:
                    raise ValueError("Social Security Number must be a valid number and of the correct format: E.x 020901-2690")
        raise ValueError("Social Security Number is not of the correct format XXXXXX-XXXX")

    def errorCheckPhone(self, phoneNumber) -> True:
        """ Checks if Phone number user input is valid, if so returns True, if not raises ValueError """
        # Format we want is XXX-XXXX
        self.checkEmpty(phoneNumber)
        if "-" in phoneNumber: # Checks if there is a - in the string
            phone_split = phoneNumber.split("-") # Split the string up
            if len(phone_split[0]) == 3 and len(phone_split[1]) == 4: # Checks if the split strings are of the correct lenght for the format
                if phone_split[0].isnumeric() and phone_split[1].isnumeric(): # And that they are for sure numbers
                    return True
        raise ValueError("Phone number is not of the correct format XXX-XXXX")
        
    def errorCheckEmail(self, email) -> True:
        """ Checks if email user input is valid, if so returns True, if not raises ValueError """
        self.checkEmpty(email) # Checks if its empty
        if not "@" in email: # And that it has an @
            raise ValueError("Email must contain an @")
        return True
    
    def errorCheckEmployeePreviousTask(self, previousTask) -> True:
        """ Function checks if the previous task is a number """
        # A Contractor can have one or many previous tasks so the user will input either 1 maintenance id or multiple
        # So the input can be something like 2 if we have maintenance id 2 or 2,4,6
        if "," in previousTask: # Meaning its a list of numbers
            tasks = previousTask.split(",") # split into the maintenance numbers on
            for task in tasks:
                if not task.isnumeric():
                    raise ValueError("Previous task should be a single integer or a list of integers in the format of 1,2,3,4 with no trailing commas")
        elif not previousTask.isnumeric(): # Meaning its a single number
            raise ValueError("Previous task should be a single integer or a list of integers in the format of 1,2,3,4 with no trailing commas")
        return True

    def errorCheckEmployeePerformanceRating(self, performanceRating, can_be_empty) -> True:
        """ Checks if the performance rating is a number or a list of numbers, if so returns True, if not raises ValueError"""
        # Can be an empty field if there are no previous tasks
        if not can_be_empty: # this is either True or False, if it can be empty we just return dont need any errors if not we raise errors on wrong input
            if not performanceRating.isnumeric(): # checks if its a number
                raise ValueError("Performance Rating must be a number")
            
            elif int(performanceRating) < 0 or int(performanceRating) > 10: # And if its between 0 and 10 since we only take ratings on that scale
                    raise ValueError("Must be a number from 0-10")
        return True

    def errorCheckEmployeeOpeningHours(self, openingHours) -> True:
        """ Checks if opening hours are of the correct format, if so returns True, if not raises ValueError """
        self.checkEmpty(openingHours) # field can no be empty
        if "-" not in openingHours: # Checks if its the correct format
            raise ValueError("Opening Hours need to be of the format X-X, E.X 9:30-5:30")
        return True

    def errorCheckBoolean(self, input) -> True:
        """ Checks if input is boolean, if so returns True, if not raises ValueError"""
        if input.lower() in ["true", "false"]: # "Boolean checker", its not really booleans that we are storing but its true or false in string form
            return True 
        raise ValueError("Input should be either a True or False")
    
    def checkErrorStartDate(self, input, datetime_format) -> True:
        """ Checks if start daate it of the correct datetime format, if so returns True, if not raises ValueError"""
        try:
            conversion = datetime.strptime(input, datetime_format) # Tries to convert the date to datetime according to date format 
            return conversion
        except ValueError: # If it cant then its the wrong format
            raise ValueError("Invalid Date format. Please input date as 'DD.MM.YYYY.HH:MM'.")

    def checkErrorEndDate(self, input, datetime_format, startDate) -> True: 
        """ Checks if enddate is of the correct datetime format and is not before startDate, if so returns True, if not raises ValueError"""
        try:
            conversion = datetime.strptime(input, datetime_format) # Tries to convert the date to datetime according to date format 
        except ValueError:
            raise ValueError("Invalid Date format. Please input date as 'DD.MM.YYYY.HH:MM'.")  # If it cant then its the wrong format

        if conversion < startDate: # But we also have to check if the end date is less than the start Date, because the end date can not be before the start date....
                raise ValueError("End Date can not be before the Start Date")
        
        if conversion == startDate: # Check also if its the exact same time
            raise ValueError("End Date can not be at the exact same time as the Start Date")

        return conversion
    
    def checkErrorStatusMaintenance(self, input) -> True:
        """ Checks if input is either ongoing or closed, if so returns True, if not raises ValueError"""
        if input.lower() in ["ongoing"]: # Checks if its one of the two inputs that should be possible
            return True
        raise ValueError("Maintenance Tasks can only be Ongoing when creating")

    def checkErrorPriority(self, input) -> True:
        """ Checks if input (priority) is one of the three possible priorities, if so returns True, if not raises ValueError"""
        if input.lower() in ["asap", "now", "emergency"]: # Checks if its one of the three inputs that should be possible
            return True
        raise ValueError("Maintenance Tasks only have three priorties, ASAP, Now or Emergency")

    def checkErrorTaskType(self, input) -> True:
        """ Checks if Task Type is one of two possible, if so returns True, if not raises ValueError"""
        # Type should be either Standard or Abnormal
        if input.lower() in ["normal", "abnormal"]:
            return True
        raise ValueError("Task Type can only either be Normal or Abnormal")

    def checkErrorFrequency(self, input) -> True:
        """ Checks if input (Frequency) is one of three possible frequencies, if so returns True, if not raises ValueError"""
        # Frequency is going to be either Daily, Weekly, Monthly, Yearly
        if input.lower() in ["daily", "weekly", "monthly", "yearly"]:
            return True
        raise ValueError("Frequency can only be: Daily, Weekly, Monthly or Yearly")

    def checkErrorContractorCost(self, input) -> True:
        """ Checks if contractor cost is a number, if so returns True, if not raises ValueError"""
        # Must be a number inside the string
        if not input.isnumeric():
            raise ValueError("Cost must be a valid number")
        return True
    
    def checkIfNumberIsNegative(self, input) -> True:
        """ Function checks if an input is a negative number"""
        self.checkNumber(input) # First check if its a number
        num = int(input)
        if num < 0:
            raise ValueError("This can not be a negative number")
        else:
            return True