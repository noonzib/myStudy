from lxml import etree
parser = etree.XMLParser(remove_blank_text=True)
with open('data.xml', 'r') as file:
	data = file.read()
#print data

elem = etree.XML(data, parser = parser)
print etree.tostring(elem)