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

country_population = []
countries = parse_and_remove('C:\mondial-3.0.xml', 'country')
for country in countries:
    name = country.attrib['name']
    population = country.attrib['government']
    country_population.append((population))

# Retrieve unique values from XML for 'government'
unique_list = []  # intilize a null list
for x in country_population: # traverse for all elements
    if x not in unique_list: # check if exists in unique_list or not
        unique_list.append(x)
print(*unique_list, sep=", ")


