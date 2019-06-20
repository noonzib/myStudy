import xml.etree.ElementTree as ET

tree = ET.parse('./data.xml')
root = tree.getroot()

ftext = "2011"
ttext = "7777"

cnt = 0
print root.tag, root.attrib
def findChild(parent, cnt):
	cnt += 1 
	
	for child in parent:
		if child != "":
			print "\t|"*cnt+'-->',child.tag, child.attrib, child.text#, "" if child.text.isspace() else child.text	
			findChild(child, cnt)
		else:
			break
	pass

def findAll():
	for child in root.iter('*'):
		print child.tag,child.attrib,child.text
	pass

def changeAllText():
	global ftext, ttext
	for child in root.iter('*'):
		if child.text == ftext:
			child.text = ttext
			print child.text
			child.set('updated', 'yes')
			print "changed the text"
			pass
	tree.write('data.xml')
	pass

def changeChooseText():
	idx = 1 
	imsi = 0
	global ftext, ttext
	for child in root.iter('*'):
		if child.text == ftext:
			child.text = ttext
			print child.text
			child.set('updated', 'yes')
			print "changed the text"
			pass
	tree.write('data.xml')
	pass

#changeAllText()
findChild(root, cnt)
findAll()