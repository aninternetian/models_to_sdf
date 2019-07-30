import xml.etree.ElementTree as ET

tree = ET.parse('model.config')
root = tree.getroot()

for elem in root.iter('model'):
    elem.set('name', 'test')

for elem in root.getiterator():
    try:
        elem.text = elem.text.replace('change', 'test')
    except AttributeError:
        pass

tree.write('model.config', xml_declaration=True, encoding='utf-8')