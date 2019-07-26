import os
import shutil

## reference
# Copy multiple files in Python - https://stackoverflow.com/questions/3397752/copy-multiple-files-in-python

#-----

## setup

# def InputFolder():    # user input folder to copy
# def OutputFolder():   # user input folder to paste
# def SourceFolder():   # `/models_to_sdf/templates/`

#-----

## make directories
os.makedirs('/OutputFolder/meshes')     # using name from InputFolder

#-----

## copy stuff going on here

# def SdfCopy():     # copies sdf files
src = '/models_to_sdf/templates/'
dest = 'OutputFolder/'

src_files = os.listdir(src)
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)

# def MeshesCopy():     # copy contents of original folder into meshes
src = '/InputFolder/'
dest = 'OutputFolder/meshes'

src_files = os.listdir(src)
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)