import json
import xml.etree.ElementTree as ET


class XMLParserIter:
    """ Process XML fragments while they are parsed """

    def __init__(self, filename, ignore_attributes=None):
        self.filename = filename
        self.current_path = []
        self.last_path = None
        self.ignore_attributes = []
        if ignore_attributes:
            self.ignore_attributes = ignore_attributes.split(',')

    def parse(self, export=False):
        it = ET.iterparse(self.filename, events=("start", "end"))
        for event, el in it:
            if event == "start":
                if "}" in el.tag:
                    el.tag = el.tag.split("}", 1)[1]  # strip all namespaces
                for attrib in el.attrib.keys():  # strip namespaces of attributes too
                    if "}" in attrib:
                        new_attrib = attrib.split("}", 1)[1]
                        el.attrib[new_attrib] = el.attrib[attrib]
                        del el.attrib[attrib]
                path = el.tag
                if el.attrib and el.tag not in self.ignore_attributes:
                    attribs = ";".join(
                        map(lambda x: f"{x[0]}={x[1]}", el.attrib.items())
                    )
                    path += "/{%s}" % attribs
                self.current_path.append(path)
            if event == "end":
                full_path = "/".join(self.current_path)

                if full_path != self.last_path:
                    self.last_path = full_path
                if el.text:
                    print(full_path)
                    print(json.dumps(el.text))
                self.current_path.pop()
