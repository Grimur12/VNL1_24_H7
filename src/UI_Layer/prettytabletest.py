from prettytable import PrettyTable
from Models.Workers import Employee

testing = Employee(1,"Grimur","023030-1111","University of Iceland","888-1122","999-2211","grimur@ru.is","University of Reykjavik","Manager")

table = PrettyTable()
table.add_rows(list(testing.__dict__.values()))

