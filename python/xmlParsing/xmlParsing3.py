import xml.etree.ElementTree as ET
from lxml import etree

parser = etree.XMLParser(remove_blank_text=True)
with open('data.xml', 'r') as file:
	data = file.read()
elem = etree.XML(data, parser = parser)
root = ET.fromstring(etree.tostring(elem))

# print data
# print etree.tostring(elem)

# tree = ET.parse('./data.xml')
# root = tree.getroot()

cnt = 0

def findChild(parent, cnt):
	if cnt == 0:
		print root.tag, root.attrib
		pass
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
		print child.tag,child.text
	pass

def changeAllText(ftext, ttext):
	token = 0
	for child in root.iter('*'):
		if child.text == ftext:
			child.text = ttext
			print child.text
			child.set('updated', 'yes')
			print "changed the text"
			token = 1
			pass
	if token != 0:
		tree.write('data.xml')
		pass
	else:
		print "Can't find the text"
	pass

def changeChooseText(ftext,ttext,idx): 
	imsi = 0
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

def printText(parent,cnt):
	cnt += 1
	for child in parent:
		print "\t|"*cnt+'-->',child.text
		printText(child,cnt)
		pass
	pass

#findChild(root, cnt)
#findAll()
#printText(root,cnt)
########################Replace text###########################
idx = 2
ftext = "7777"
ttext = "8888"
#changeAllText(ftext, ttext)
#changeChooseText(ftext,ttext,idx)
###############################################################

print root[1][2].text[5]










