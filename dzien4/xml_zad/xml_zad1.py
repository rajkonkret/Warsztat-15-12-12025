# xml - język tagów
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

tom = Element("autokomis")

sam1 = SubElement(tom, "samochod")
id = SubElement(sam1, "id")
id.text = 'sam1'

marka = SubElement(sam1, "marka")
marka.text = "Toyota"

rok = SubElement(sam1, "rok")
rok.text = "2025"

cena = SubElement(sam1, "cena")
cena.text = "56000"

xml_string = tostring(tom, "UTF-8")
print(xml_string)


def pretty(element):
    xml_string = tostring(element, "UTF-8")
    rep = minidom.parseString(xml_string)
    return rep.toprettyxml(indent="\t")


xml_string = pretty(tom)
with open("toyota.xml", "w", encoding="utf-8") as f:
    f.write(xml_string)

    # <?xml version="1.0" ?>
    # <autokomis>
    # 	<samochod>
    # 		<id>sam1</id>
    # 		<marka>Toyota</marka>
    # 		<rok>2025</rok>
    # 		<cena>56000</cena>
    # 	</samochod>
    # </autokomis>
