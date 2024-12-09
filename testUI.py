from prettytable import PrettyTable
mainMenu = PrettyTable()

mainMenu.field_names = ["Main menu"]
mainMenu.add_row(["1. View destinations"])
mainMenu.add_row(["2. View properties"])
mainMenu.add_row(["3. View employees"])
mainMenu.add_row(["4. View contractors"])
mainMenu.add_row(["5. View managers"])
mainMenu.add_row(["6. View active tasks"])
mainMenu.add_row(["7. Make a report"])
mainMenu.add_row(["b. Back"])
mainMenu.add_row(["q. Quit"])
mainMenu.align = 'l'
print(mainMenu)

destionationMenu = PrettyTable()
destinationMenu.add_row(["1. Reykjavik"])
destinationMenu.add_row(["2. Nuuk"])
destinationMenu.add_row(["3. Kulusuk"])
destinationMenu.add_row([])
destinationMenu.add_row([])
destinationMenu.add_row([])

destionationMenu.add