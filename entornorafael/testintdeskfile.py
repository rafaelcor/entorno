#coding=utf-8

import xml.dom.minidom
xmldoc = xml.dom.minidom.parse("test.deskfile")

for n in xmldoc.childNodes :
	for contacto in n.childNodes:
		for registro in contacto.childNodes:
			if registro.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
				print registro.nodeName , ":" , registro.firstChild.data
