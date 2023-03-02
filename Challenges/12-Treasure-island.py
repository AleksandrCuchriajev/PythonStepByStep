row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
selected_cell = input("please enter column number and row number, for example 12 : ")
vertical = int(selected_cell[0])
horizontal = int(selected_cell[1])
selection_horizontal = map[horizontal - 1]
# selection_horizontal[vertical-1]="X"
map[horizontal - 1][vertical - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
