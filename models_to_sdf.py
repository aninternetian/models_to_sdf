import os
import argparse
import shutil
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Copy models and textures from exported folder', required = True)
parser.add_argument('--output', help='Paste everything into folder', required = True)
args = parser.parse_args()
folderInput = args.input
folderOutput = args.output

inputFolderName = os.path.basename(folderInput)

meshesDir = os.path.join(folderOutput, inputFolderName, 'meshes')
os.makedirs(meshesDir)

# copies contents of one folder to another yay
def CopyFiles(usrInput, usrOutput):
    src_files = os.listdir(usrInput)
    for file_name in src_files:
        full_file_name = os.path.join(usrInput, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, usrOutput)

CopyFiles(folderInput, meshesDir)

templatesDir = os.path.join(os.getcwd(), 'templates')

sdfDir = os.path.join(folderOutput, inputFolderName)

CopyFiles(templatesDir, sdfDir)

## xml editing

def replaceValue(path):
    tree = ET.parse(path)
    root = tree.getroot()

    for elem in root.iter('model'):
        if elem.get('name') is not None:
            elem.set('name', inputFolderName)

    for elem in root.getiterator():
            elem.text = elem.text.replace('change', inputFolderName)

    tree.write(path, xml_declaration=True, encoding='utf-8')

sdfPath = os.path.join(sdfDir, 'model.sdf')
configPath = os.path.join(sdfDir, 'model.config')
replaceValue(sdfPath)
replaceValue(configPath)