import xml.etree.ElementTree as ET

tree = ET.parse('./data.xml')
root = tree.getroot()

print root.tag, root.attrib

for child in root:
    print ' |-->',child.tag, child.attrib
    for child2 in child:
     	print ' |\t\t|-->',child2.tag, child2.attrib, child2.text
   #   	for child3 in child2:
			# print ' |\t\t|\t\t|-->',child3.tag, child3.attrib, child3.text    		

# for neighbor in root.iter('*'):
#  	print neighbor.tag, neighbor.attrib