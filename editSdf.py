# currently generating an extra tag in model.config that shouldn't be there
import xml.etree.ElementTree as ET

def replaceValue(path):
    tree = ET.parse(path)
    root = tree.getroot()

    for elem in root.iter('model'):     # only working for model.sdf
        elem.set('name', 'test')

    for elem in root.getiterator():
        try:
            elem.text = elem.text.replace('change', 'test')
        except AttributeError:
            pass

    tree.write(path, xml_declaration=True, encoding='utf-8')