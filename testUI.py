from prettytable import PrettyTable
main_menu_1 = PrettyTable()

main_menu_1.field_names = ["Main menu"]
main_menu_1.add_row(["1. View destinations"])
main_menu_1.add_row(["2. View properties"])
main_menu_1.add_row(["3. View employees"])
main_menu_1.add_row(["4. View contractors"])
main_menu_1.add_row(["5. View managers"])
main_menu_1.add_row(["6. View active tasks"])
main_menu_1.add_row(["7. Make a report"])
main_menu_1.add_row(["b. Back"])
main_menu_1.add_row(["q. Quit"])
main_menu_1.align = 'l'
print(main_menu_1)

menu_1.field_names = ["View destination"]
menu_1.add_row([])
menu_1.add_row([])
menu_1.add_row([])
menu_1.add_row([])
menu_1.add_row([])
menu_1.add_row([])
