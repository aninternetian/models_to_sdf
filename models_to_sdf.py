import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Copy models and textures from exported folder', required = True)
parser.add_argument('--output', help='Paste everything into folder', required = True)
args = parser.parse_args()
input = args.input       # ~/Documents/Prev/hospital/beds/CGMClassic
output = args.output    # ~/Documents/work/test/

inputFolderName = os.path.basename(input)

meshesDir = os.path.join(output, inputFolderName, 'meshes')      # /home/roselle/Documents/work/test/beds/meshes
os.makedirs(meshesDir)

# copies contents of one folder to another yay
def CopyFiles(input, output):
    src_files = os.listdir(input)
    for file_name in src_files:
        full_file_name = os.path.join(input, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, output)

CopyFiles(input, meshesDir)

templatesDir = os.path.join(os.getcwd(), 'templates')

sdfDir = os.path.join(output, inputFolderName)
print(sdfDir)

CopyFiles(templatesDir, sdfDir)