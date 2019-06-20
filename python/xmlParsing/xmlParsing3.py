import xml.etree.ElementTree as ET

tree = ET.parse('./data.xml')
root = tree.getroot()

ftext = "7777"
ttext = "8888"

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

def changeChooseText(idx): 
	imsi = 0
	global ftext, ttext
	for child in root.iter('*'):
		if child.text == ftext:
			imsi+=1
			if imsi==idx:
				child.text = ttext
				print child.text
				child.set('updated', 'yes')
				tree.write('data.xml')
				print "changed the text"
				return
	print "Can't find the text"
	pass

# findChild(root, cnt)
# findAll()
# changeAllText()
idx = 2
changeChooseText(idx)