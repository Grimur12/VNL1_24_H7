# Error checker class for all error checks

class ErrorCheckers:
    def __init__(self) -> None:
        pass

    def errorCheckName(self, name):
        """ Checks if name user input is valid """
        if name.isnumeric():
            raise ValueError("Name must not be a number")
        return True
    
    def errorCheckAddress(self, address):
        """ Checks if Address user input is valid """
        if address.isnumeric():
            raise ValueError("Address must not be just a number")
        return True

    def errorCheckSocialSecurity(self, socialSecurity):
        """ Checks if Social Security number user input is valid """
        # Format we want is XXXXXX-XXXX
        if "-" in socialSecurity:
            social_split = socialSecurity.split("-")
            if len(social_split[0]) == 6 and len(social_split[1]) == 4:
                if social_split[0].isnumeric() and social_split[1].isnumeric():
                    return True
        raise ValueError("Social Security Number is not of the correct format XXXXXX-XXXX")

    def errorCheckPhone(self, phoneNumber):
        """ Checks if Phone number user input is valid """
        # Format we want is XXX-XXXX
        if "-" in phoneNumber:
            phone_split = phoneNumber.split("-")
            if len(phone_split[0]) == 3 and len(phone_split[1]) == 4:
                if phone_split[0].isnumeric() and phone_split[1].isnumeric():
                    return True
        raise ValueError("Phone number is not of the correct format XXX-XXXX")
        
    def errorCheckEmail(self, email):
        """ Checks if email user input is valid """
        if not "@" in email:
            raise ValueError("Email must contain an @")
        return True

    def errorCheckLocation(self, location):
        """ Checks if location user input is valid """
        if location.isnumeric():
            raise ValueError("Location must not be just a number")
        return True

    def errorCheckEmployeeType(self, type):
        """ Checks if type user input is valid """
        valid_types = ["General", "Manager"]
        if type not in valid_types:
            raise ValueError("Type is not Valid, must be a Manager, General or Contractor")
        return True
    
    def errorCheckContractorType(self, type):
        if type != "Contractor":
            raise ValueError("Type is not Valid, must be a Contractor")
        return True

