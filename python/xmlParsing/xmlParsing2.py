import xml.etree.ElementTree as ET

tree = ET.parse('./data.xml')
root = tree.getroot()

print root.tag, root.attrib
cnt = 0

def findChild(parent, cnt):
	cnt += 1 
	for child in parent:
		if child != "":
			print " |"+"\t"*cnt+'|-->',child.tag, child.attrib, child.text
			findChild(child, cnt)
		else:
	 		break

for child in root:
    print ' |-->',child.tag, child.attrib
    cnt = 1
    findChild(child, cnt)  		

# for neighbor in root.iter('*'):
#  	print neighbor.tag, neighbor.attrib