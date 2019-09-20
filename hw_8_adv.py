import xml.etree.ElementTree as ET

def parse_and_remove(filename, path):
   path_parts = path.split('/')
   doc = ET.iterparse(filename, ('start', 'end'))
   # Skip root element
   next(doc)
   tag_stack = []
   elem_stack = []
   for event, elem in doc:
    if event == 'start':
      tag_stack.append(elem.tag)
      elem_stack.append(elem)
    elif event == 'end':
                if tag_stack == path_parts:
                    yield elem
                try:
                    tag_stack.pop()
                    elem_stack.pop()
                except IndexError:
                    pass

country_list = []
country_government = []
countries = parse_and_remove('C:\mondial-3.0.xml', 'country')

for country in countries:
    name = country.attrib['name']
    country_list.append(name)
    government = country.attrib['government']
    country_government.append((name, government))
    country_government_dict = dict(country_government)

#Country Names that contain several parts (like Bosnia and Herzegovina)
matching = [s for s in country_list if " " in s]

#Retrieve governmenr type for Countries that contain several parts in the name (like Bosnia and Herzegovina)
government_list = []
for key, value in country_government_dict.items():
    if key in matching:
        government_list.append(value)

# Retrieve unique values from XML for 'government'
unique_list = []  # intilize a null list
for x in government_list: # traverse for all elements
    if x not in unique_list: # check if exists in unique_list or not
        unique_list.append(x)
print(*unique_list, sep=", ")


