from prettytable import PrettyTable
table = PrettyTable() #create a new object

# 2 parameters: add_column(Name of column, datas)
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

#change object attributes
table.align = "l" #change from center to left align
print(table)




