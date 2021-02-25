# Get the Data Table collection
print Document.Data.Tables

# Printing the Object ID of individual Data Table
for i in Document.Data.Tables:
	print i

# Printing the DT name
for i in Document.Data.Tables:
	print i.Name

# Accessing individual DT
print Document.Data.Tables.TryGetValue('airbnb - AirBnB_NYC') # returns a tuple (Bool, obj ID)

# OR
print Document.Data.Tables['airbnb - AirBnB_NYC']


# Get the columns collection:
dt = Document.Data.Tables['airbnb - AirBnB_NYC']
collColumns = dt.Columns
print collColumns


# Get Individual Column
for i in collColumns:
	print i.Name

# Extract one column:
print collColumns['Room Type']


from Spotfire.Dxp.Data import *
# Creating empty indexset
emptyIndexSet = IndexSet()
print emptyIndexSet.Capacity
print emptyIndexSet.Count

# Creating IndexSet on a Data Table
IndexSet1 = IndexSet(dt.RowCount, True) # True to include the rows in the first parameter, False to exclude the rows in the first param
print IndexSet1.Count
print IndexSet1.Capacity
print IndexSet1.First
print IndexSet1.Last

# IndexSet on specific set of rows
indexSetSelection = IndexSet(dt.RowCount, dt.Select('[Room Type] = "Private room"')) # Second parameter is the condition to look for
print indexSetSelection.Count

rowSelection = RowSelection(indexSetSelection)
print rowSelection.IncludedRowCount

rowSelectionSelect = dt.Select('[Room Type] = "Private room"')
print rowSelectionSelect.IncludedRowCount

# Rowselection to IndexSet
rowIndex = rowSelectionSelect.AsIndexSet()
print rowIndex.Capacity
