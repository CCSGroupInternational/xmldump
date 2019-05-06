import xml.etree.ElementTree as ET
import sys


def xml_parse(filename):
    """ """
    # instead of ET.fromstring(xml)
    it = ET.iterparse(filename)
    for _, el in it:
        if "}" in el.tag:
            el.tag = el.tag.split("}", 1)[1]  # strip all namespaces
        for attrib in el.attrib.keys():  # strip namespaces of attributes too
            if "}" in attrib:
                new_attrib = attrib.split("}", 1)[1]
                el.attrib[new_attrib] = el.attrib[attrib]
                del el.attrib[attrib]
    return it.root


my_parse = xml_parse(sys.argv[1])
print(my_parse)
