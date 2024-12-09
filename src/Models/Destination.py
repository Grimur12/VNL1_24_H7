# Here is our Destination class

class Destination:
    def __init__(self, name, destinationID, country, timezone, airportName, phoneNumber, openingHours, managerOfDestination,):
        """ Defines variables for Destination """
        self.name = name
        self.destinationID = destinationID
        self.country = country
        self.timezone = timezone
        self.airportName = airportName
        self.phoneNumber = phoneNumber
        self.openingHours = openingHours
        self.managerOfDestination = managerOfDestination

    def Destination_Dict(self) -> dict:
        """ Returns all the variables in our Destination class into a dictionary """
        return {
        "name": self.name,
        "destinationID": self.destinationID,
        "country": self.country,
        "timezone": self.timezone,
        "airportName": self.airportName,
        "phone number": self.phoneNumber,
        "openingHours": self.openingHours,
        "managerOfDestination": self.managerOfDestination
        }

class Reykjavik(Destination):
    pass

class Nuuk(Destination):
    pass

class Kulusuk(Destination):
    pass

class Thorshofn(Destination):
    pass

class Tingwall(Destination):
    pass

class Longyearbyen(Destination):
    pass
    
