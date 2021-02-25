from Spotfire.Dxp.Data import *

collDt = Document.Data.Tables
collMarking = Document.Data.Markings
dt = collDt['Orders']

collCols = dt.Columns
col = collCols['Sub-Category']

# Create indexset on the rows you want to select
indSet = IndexSet(dt.RowCount, True)

# Create a cursor for the column
colCursor = DataValueCursor.Create[str](col, True)

# retrieve the values
rows = dt.GetRows(indSet, colCursor)
"""
for row in rows:
	print colCursor.CurrentValue
"""
# Floating point cursor
col = collCols['Sales']

# Create indexset on the rows you want to select
indSet = IndexSet(dt.RowCount, True)
colCursor = DataValueCursor.Create(col)
rows = dt.GetRows(indSet, colCursor)
"""
for row in rows:
	print colCursor.CurrentValue
"""

# Integer

col = collCols['Quantity']

# Create indexset on the rows you want to select
indSet = IndexSet(dt.RowCount, True)
colCursor = DataValueCursor.CreateNumeric(col)
rows = dt.GetRows(indSet, colCursor)

"""
for row in rows:
	print colCursor.CurrentValue

"""

# Time

col = collCols['Ship Date']

# Create indexset on the rows you want to select
indSet = IndexSet(dt.RowCount, True)
colCursor = DataValueCursor.CreateTime(col)
rows = dt.GetRows(indSet, colCursor)
"""
for row in rows:
	print colCursor.CurrentValue, type(colCursor.CurrentValue)
"""

# Marked Rows
marking = collMarking['Marking']
markedRows = marking.GetSelection(dt)
colCursor = DataValueCursor.CreateTime(col)
rows = dt.GetRows(markedRows.AsIndexSet(), colCursor)
"""
for row in rows:
	print colCursor.CurrentValue
"""

# Filtered rows
filterPanel = Document.ActivePageReference.FilterPanel
filterScheme = filterPanel.FilteringSchemeReference
filterCollection = filterScheme[dt]
filterIndexSet = filterCollection.FilteredRows
colCursor = DataValueCursor.CreateTime(col)
rows = dt.GetRows(filterIndexSet, colCursor)
"""
for row in rows:
	print colCursor.CurrentValue
"""

# Creating cursor on multiple columns

collCursors = []
collCursors = [DataValueCursor.CreateFormatted(i) for i in collCols if i.Name in ['Category', 'Ship Date','Sub-Category','Quantity']]
rows = dt.GetRows(filterIndexSet, tuple(collCursors))
"""
for row in rows:
	print collCursors[0].CurrentValue, collCursors[1].CurrentValue, collCursors[2].CurrentValue, collCursors[3].CurrentValue
"""

# with data types
collCursorsColumns = [col for col in collCols if col.Name in ['Category', 'Country','City','Quantity']]
dataTypes = [str, str, str, int]
collCursors = [DataValueCursor.Create[dataTypes[i]](col) for i, col in enumerate(collCursorsColumns)]
rows = dt.GetRows(filterIndexSet, tuple(collCursors))
"""
for row in rows:
	print collCursors[0].CurrentValue, collCursors[1].CurrentValue, collCursors[2].CurrentValue, collCursors[3].CurrentValue
"""

# Columns Manipulation
"""
if collCols.Contains("Price"):
	collCols.Remove('Price')
"""

# Create a calculated column:
collCols.AddCalculatedColumn("NewCaculatedColumns","[Sales]*2")
# option to freeze the calculated column from inheriting from its parent columns
collCols['NewCaculatedColumns'].As[CalculatedColumn]().Freeze()
