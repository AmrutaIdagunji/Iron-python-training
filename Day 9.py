# Working with pages
collPages = Document.Pages

# Printing page names
"""
for i in collPages:
	print i.Title
"""

# accessing visuals in a page
"""
vizTitle = [viz.Title for i in collPages for viz in i.Visuals]
print vizTitle
"""

# accessing a particular type of visual
"""
vizTitle = [viz.Title for i in collPages for viz in i.Visuals if viz.TypeId.DisplayName == "Text area"]
print vizTitle
"""

# Accessing single page
"""
print collPages.Item[0].Title
print collPages.Item[1].Title
"""

# using the title to access the page
page = [page for page in collPages if page.Title == "Page"][0]
print page.Title

# setting a page as active page 
Document.ActivePageReference = page

# Panels
"""
panel = [panel.Title for page in collPages for panel in page.Panels if panel.Title == "Filters"]
print panel
"""

# Filtering Scheme
"""
panel = [panel.FilteringSchemeReference for page in collPages for panel in page.Panels if panel.Title == "Filters"]
print panel
"""

# Adding duplicate page and change the title of the duplicate page
"""
collPages.AddDuplicate(page)
page = [page for page in collPages if page.Title == "Page (2)"][0]
page.Title = "Page duplicate"
print page.Title
"""

# create a new page
"""
collPages.AddNew("NewPage")
page = [page for page in collPages if page.Title == "NewPage"][0]
print page.Title
"""

# Change the navigation mode
from Spotfire.Dxp.Application import PageNavigationMode
collPages.NavigationMode = PageNavigationMode.Links #PageNavigationMode.Tabs | PageNavigationMode.None

# Remove a page
"""
collPages.Remove(collPages[2])
"""

# Remove at 
"""
collPages.RemoveAt(2)
"""
