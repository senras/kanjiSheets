import xml.sax.handler


class BasicHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self.elementsTree = []

    def currentElement(self):
        return str(self.elementsTree[-1])

    def startElement(self, qName, atts):
        self.elementsTree.append(str(qName))
        attrName = "handle_start_" + str(qName)
        if hasattr(self, attrName):
            rfunc = getattr(self, attrName)
            rfunc(atts)
        self.characters = ""
        return True

    def endElement(self, qName):
        attrName = "handle_data_" + qName
        if hasattr(self, attrName):
            rfunc = getattr(self, attrName)
            rfunc(self.characters)
        attrName = "handle_end_" + str(qName)
        if hasattr(self, attrName):
            rfunc = getattr(self, attrName)
            rfunc()
        self.elementsTree.pop()
        return True

    def characters(self, string):
        self.characters += string
        return True
