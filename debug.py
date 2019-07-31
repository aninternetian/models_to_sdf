import os
import shutil

folderInput = '/home/roselle/Documents/Prev/hospital/beds/CGMClassic'
folderOutput = '/home/roselle/Documents/work/test/'

def CreateFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Folder already exists')

def CopyFiles(input, output):
    src_files = os.listdir(input)
    for file_name in src_files:
        full_file_name = os.path.join(input, file_name)
        if os.path.isfile(CreateFolder(full_file_name)):
            shutil.copy(full_file_name, output)

def CopyFiles(input, output):
    src_files = os.listdir(input)
    for file_name in src_files:
        full_file_name = os.path.join(input, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, output)

CopyFiles(folderInput, folderOutput)