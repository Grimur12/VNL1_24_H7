# Error checker class for all error checks

class ErrorCheckers:
    def __init__(self) -> None:
        pass

    def checkEmployeeInput(self, params):
        """ Checks for errors in user input for creating employees, returns None if wrong input otherwise True """
        # Params we should be getting are
        # XXXXXX-XXXX
        # [name, address, socialSecurity, atHomePhone, gsm, email, workLocation, employeeType] for employees

        if params[0].isnumeric():
            return None
        else:
            return True
        
        if params[1].isnumeric():
            return None
        else: return True

        if "-" in params[2]:
            social_split = params[2].split("-")
            if len(social_split[0]) == 6 and len(social_split[1] == 4):
                if social_split[0].isnumeric() and social_split[1].isnumeric():
                    return True
        else:
            return None
    
    def checkContractorInput(self, params):
        
        # Params we should be getting are 
        # [name, address, socialSecurity, atHomePhone, gsm, email, workLocation, employeeType, previousTask, performanceRating, contractorContact, openingHours]
        if self.checkEmployeeInput(params[:8]): #Use checkemployee for first 8 since they are common in both
            #If it passes check the rest of the unique contractor params


    def checkManagaerInput(self, params):
        pass


    
