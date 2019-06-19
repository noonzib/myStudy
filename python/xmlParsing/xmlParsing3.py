import xml.etree.ElementTree as ET

tree = ET.parse('./data.xml')
root = tree.getroot()

print root.tag, root.attrib
cnt = 0

def findChild(parent, cnt):
	cnt += 1 
	for child in parent:
		if child != "":
			print "\t|"*cnt+'-->',child.tag, child.attrib#, "" if not(child.text.isalpha()) else child.text	
			findChild(child, cnt)
		else:
	 		break

findChild(root,cnt)

