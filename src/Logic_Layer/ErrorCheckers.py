# Error checker class for all error checks
from datetime import datetime

class ErrorCheckers:

    def __init__(self) -> None:
        pass
    
    def checkNumber(self, input) -> True:
        """ Returns True if user input is a number, raises ValueError otherwise"""
        # Used to check both for input when changing information and as count.
        try:
            int(input)
        except ValueError:
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
        self.checkEmpty(name)
        if name.isnumeric():
            raise ValueError("Name must not be a number")
        return True
    
    def errorCheckAddress(self, address) -> True:
        """ Checks if Address user input is valid, if so returns True, if not raises ValueError """
        self.checkEmpty(address)
        if address.isnumeric():
            raise ValueError("Address must not be just a number")
        return True

    def errorCheckSocialSecurity(self, socialSecurity) -> True:
        """ Checks if Social Security number user input is valid, if so returns True, if not raises ValueError """
        # Format we want is XXXXXX-XXXX
        self.checkEmpty(socialSecurity)
        if "-" in socialSecurity:
            social_split = socialSecurity.split("-")
            if len(social_split[0]) == 6 and len(social_split[1]) == 4:
                if social_split[0].isnumeric() and social_split[1].isnumeric():
                    return True
        raise ValueError("Social Security Number is not of the correct format XXXXXX-XXXX")

    def errorCheckPhone(self, phoneNumber) -> True:
        """ Checks if Phone number user input is valid, if so returns True, if not raises ValueError """
        # Format we want is XXX-XXXX
        self.checkEmpty(phoneNumber)
        if "-" in phoneNumber:
            phone_split = phoneNumber.split("-")
            if len(phone_split[0]) == 3 and len(phone_split[1]) == 4:
                if phone_split[0].isnumeric() and phone_split[1].isnumeric():
                    return True
        raise ValueError("Phone number is not of the correct format XXX-XXXX")
        
    def errorCheckEmail(self, email) -> True:
        """ Checks if email user input is valid, if so returns True, if not raises ValueError """
        self.checkEmpty(email)
        if not "@" in email:
            raise ValueError("Email must contain an @")
        return True
    
    def errorCheckEmployeePreviousTask(self, previousTask) -> True:
        """ .. not fully implemented """
        # this function needs to check if we have that task in our Maintenance DB either by ID or name
        if previousTask.isnumeric():
            raise ValueError("previousTask can not be just numeric")
        return True

    def errorCheckEmployeePerformanceRating(self, performanceRating) -> True:
        """ Checks if the performance rating is a number, if so returns True, if not raises ValueError"""
        if not performanceRating.isnumeric():
            raise ValueError("Performance Rating must be a number")
        
        elif int(performanceRating) < 0 or int(performanceRating) > 10:
                raise ValueError("Must be a number from 0-10")
        return True

    def errorCheckEmployeeOpeningHours(self, openingHours) -> True:
        """ Checks if opening hours are of the correct format, if so returns True, if not raises ValueError """
        self.checkEmpty(openingHours)
        if "-" not in openingHours:
            raise ValueError("Opening Hours need to be of the format X-X, E.X 9:30-5:30")
        return True

    def errorCheckBoolean(self, input) -> True:
        """ Checks if input is boolean, if so returns True, if not raises ValueError"""
        if input.lower() in ["true", "false"]:
            return True
        raise ValueError("Input should be either a True or False")
    
    def checkErrorStartDate(self, input, datetime_format) -> True:
        """ Checks if start daate it of the correct datetime format, if so returns True, if not raises ValueError"""
        try:
            conversion = datetime.strptime(input, datetime_format)
            return conversion
        except ValueError:
            raise ValueError("Invalid Date format. Please input date as 'DD.MM.YYYY.HH:MM'.")
            

    def checkErrorEndDate(self, input, datetime_format, startDate) -> True: 
        """ Checks if enddate is of the correct datetime format and is not before startDate, if so returns True, if not raises ValueError"""
        try:
            conversion = datetime.strptime(input, datetime_format)
        except ValueError:
            raise ValueError("Invalid Date format. Please input date as 'DD.MM.YYYY.HH:MM'.")

        if conversion < startDate:
                raise ValueError("End Date can not be before the Start Date")

        return conversion
    
    def checkErrorStatusMaintenance(self, input) -> True:
        """ Checks if input is either ongoing or closed, if so returns True, if not raises ValueError"""
        if input.lower() in ["ongoing", "closed"]:
            return True
        raise ValueError("Maintenance Tasks can only either be Ongoing or Closed")

    def checkErrorFeedback(self, input) -> True:
        """ Checks if the input (feedback), is a number between 0 and 10, if so returns True, if not raises ValueError"""
        if input.isnumeric():
            if int(input) >= 0 and int(input) <= 10:
                return True
        raise ValueError("Feedback should be a number ranging from 0-10")

    def checkErrorPriority(self, input) -> True:
        """ Checks if input (priority) is one of the three possible priorities, if so returns True, if not raises ValueError"""
        if input.lower() in ["low", "medium", "high"]:
            return True
        raise ValueError("Maintenance Tasks only have three priorties, Low, Medium and High")

    def checkErrorTaskType(self, input) -> True:
        """ Checks if Task Type is one of two possible, if so returns True, if not raises ValueError"""
        # Type should be either Standard or Abnormal
        if input.lower() in ["normal", "abnormal"]:
            return True
        raise ValueError("Task Type can only either be Normal or Abnormal")

    def checkErrorFrequency(self, input) -> True:
        """ Checks if input (Frequency) is one of three possible frequencies, if so returns True, if not raises ValueError"""
        # Frequency is going to be either Daily, Weekly, Monthly
        if input.lower() in ["daily", "weekly", "monthly"]:
            return True
        raise ValueError("Frequency can only be: Daily, Weekly or Monthly")

    def checkErrorContractorCost(self, input) -> True:
        """ Checks if contractor cost is a number, if so returns True, if not raises ValueError"""
        # Must be a number inside the string
        if not input.isnumeric():
            raise ValueError("Cost must be a valid number")
        return True