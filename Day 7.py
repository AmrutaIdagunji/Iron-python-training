from Spotfire.Dxp.Data import *

collDt = Document.Data.Tables
collMarking = Document.Data.Markings

for i in collMarking:
	print i.Name

# Marking all rows
rows = RowSelection(IndexSet(collDt['Orders'].RowCount, True))
collMarking['Marking'].SetSelection(rows, collDt['Orders'])

# Set selection using RowSelection
# Mark a particular value
rowSelection = collDt['Orders'].Select('[City] = "Los Angeles"')
collMarking['Marking'].SetSelection(rowSelection, collDt['Orders'])

# OR operation
rowSelect1 = collDt['Orders'].Select('[Customer ID] = "BH-11710"')
rowSelect2 = collDt['Orders'].Select('[City] = "Concord"')
rowsComb = RowSelection.Combine(rowSelect1, rowSelect2, DataSelectionOperation.Add) # DataSelectionOperation.Subtract
collMarking['Marking'].SetSelection(rowsComb, collDt['Orders'])

# Set selection using IndexSet
# Get Selection - to read the rows marked
rowSelect1 = collDt['Orders'].Select('[Customer ID] = "BH-11710"')
rowSelect2 = collDt['Orders'].Select('[City] = "Los Angeles"')
Set1 = rowSelect1.AsIndexSet()
Set2 = rowSelect2.AsIndexSet()

rowsIntersect = RowSelection(IndexSet.And(Set1, Set2))
collMarking['Marking'].SetSelection(rowsIntersect, collDt['Orders'])