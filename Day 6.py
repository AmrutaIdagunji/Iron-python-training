from Spotfire.Dxp.Application.Filters import *

dtActive = Document.ActiveDataTableReference
filterPanel = Document.ActivePageReference.FilterPanel

filterScheme = filterPanel.FilteringSchemeReference 

filtercollection = filterScheme[dtActive]

for i in filtercollection:
	print i.Name

# reset all filters
filtercollection.ResetAllFilters()

# Reset a filter
filter = filtercollection['Returned']
filter.Reset()

# 
filterObject = filter.As[ListBoxFilter]()
#filterObject.Reset()
#filterObject.IncludeAllValues = False
#filterObject.SetSelection('Yes')


# Hide a filter or a tableGroup or filterPanel
# 1. Hide the panel
filterPanel.Visible= True


# 2. Hide the tableGroup
for group in filterPanel.TableGroups:
	if group.Name == "Orders":
		group.Visible = False
		print group


# 3. Hide a particular Filter
for group in filterPanel.TableGroups:
	for i in group.FilterHandles:
		if i.FilterReference.Name =="Order ID":
			i.Visible = False
			print i.FilterReference.Name


