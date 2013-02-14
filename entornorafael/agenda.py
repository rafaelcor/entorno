#!/usr/bin/python
# Nombre : xml2.py
import xml.dom.minidom
xmldoc = xml.dom.minidom.parse("test.deskfile")

for n in  xmldoc.childNodes :
    #print n.tagName
    for name in n.childNodes:
        for registro in name.childNodes:
            if registro.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
                print registro.nodeName ,":" , registro.firstChild.data
