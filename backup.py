import os
import shutil

# os.makedirs(inputFolderName)   # create folders based on input folder name

# copies contents of one folder to another yay
def CopyFiles(input, output):
    src_files = os.listdir(input)
    for file_name in src_files:
        full_file_name = os.path.join(input, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, output)

def MeshesCopy():
    meshes = os.path.join(output, 'meshes')
    CopyFiles(input, meshes)

MeshesCopy()


#----

# termplatesDir = os.path.join(os.getcwd(), 'templates')
# CopyFiles(termplatesDir, output)