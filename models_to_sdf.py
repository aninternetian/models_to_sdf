import os
import shutil
import argparse

# user input

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Copy models and textures from exported folder', required = True)
parser.add_argument('--output', help='Paste everything into folder', required = True)
args = parser.parse_args()
input = args.input
output = args.output

# retrieve name of input folder
inputFolderName = os.path.basename(input)

# SDF templates
termplatesDir = os.path.join(os.getcwd(), 'templates')

# create folders
os.makedirs(inputFolderName)

# copies contents of one folder to another yay
def CopyFiles(input, output):
    src_files = os.listdir(input)
    for file_name in src_files:
        full_file_name = os.path.join(input, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, output)

# CopyFiles(termplatesDir, output)

def MeshesCopy():
    meshes = os.path.join(output, 'meshes')
    CopyFiles(input, meshes)

MeshesCopy()