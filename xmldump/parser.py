import json
import xml.etree.ElementTree as ET


class XMLParserIter:
    """ Process XML fragments while they are parsed """

    def __init__(self, filename):
        self.filename = filename
        self.current_path = []
        self.last_path = None

    def parse(self, export=False):
        it = ET.iterparse(self.filename, events=("start", "end"))
        for event, el in it:
            if event == "start":
                if "}" in el.tag:
                    el.tag = el.tag.split("}", 1)[1]  # strip all namespaces
                self.current_path.append(el.tag)
            if event == "end":
                for attrib in el.attrib.keys():  # strip namespaces of attributes too
                    if "}" in attrib:
                        new_attrib = attrib.split("}", 1)[1]
                        el.attrib[new_attrib] = el.attrib[attrib]
                        del el.attrib[attrib]
                    full_path = '/'.join(self.current_path)
                    if full_path != self.last_path:
                        print(full_path)
                        self.last_path = full_path
                    print(json.dumps(el.attrib))
                if el.text:
                    print(json.dumps(el.text))
                self.current_path.pop()
