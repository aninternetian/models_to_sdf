import xml.etree.ElementTree as ET

def replaceValue(path):
    tree = ET.parse(path)
    root = tree.getroot()

    for elem in root.iter('model'):
        if elem.get('name') is not None:
            elem.set('name', 'test')

    for elem in root.getiterator():
            elem.text = elem.text.replace('change', 'test')

    tree.write(path, xml_declaration=True, encoding='utf-8')
