import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Copy models and textures from exported folder', required = True)
parser.add_argument('--output', help='Paste everything into folder', required = True)
args = parser.parse_args()
input = args.input       # /home/roselle/Documents/Prev/hospital/beds
output = args.output    # /home/roselle/Documents/work/test/

inputFolderName = os.path.basename(input)

path = os.path.join(output, inputFolderName, 'meshes')
os.makedirs(path)