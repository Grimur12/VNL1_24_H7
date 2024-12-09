# Here is our Destination class

class Destination:
    def __init__(self, name, destinationID, country, timezone, airportName, phoneNumber, openingHours, managerOfDestination):
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
    def __init__(self, name, destinationID, country, timezone, airportName, phoneNumber, openingHours, managerOfDestination):
        pass

class Nuuk(Destination):
    def __init__(self, name, destinationID, country, timezone, airportName, phoneNumber, openingHours, managerOfDestination):
        pass

class Kulusuk(Destination):
    def __init__(self, name, destinationID, country, timezone, airportName, phoneNumber, openingHours, managerOfDestination):
        pass

class Thorshofn(Destination):
    def __init__(self, name, destinationID, country, timezone, airportName, phoneNumber, openingHours, managerOfDestination):
        pass

class Tingwall(Destination):
    def __init__(self, name, destinationID, country, timezone, airportName, phoneNumber, openingHours, managerOfDestination):
        pass

class Longyearbyen(Destination):
    def __init__(self, name, destinationID, country, timezone, airportName, phoneNumber, openingHours, managerOfDestination):
        pass