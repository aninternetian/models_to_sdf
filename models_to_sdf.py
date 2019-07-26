import os
import shutil
import argparse

#-----

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    _, all_arguments = parser.parse_known_args()
    double_dash_index = all_arguments.index('--')
    script_args = all_arguments[double_dash_index + 1:]

    parser.add_argument('input', help='Input folder directory')
    parser.add_argument('output', help='Output folder directory')
    args, _ = parser.parse_known_args(script_args)

#    bpy.ops.wm.open_mainfile(filepath=args.input)

#-----

# templates
termplatesDir = os.path.join(os.getcwd(), 'templates')

# mkdir
os.makedirs('/OutputFolder/meshes')

# copies contents of one folder to another yay
def CopyFiles(src, dest):
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)

# sdf
CopyFiles(termplatesDir, 'OutputFolder')

def MeshesCopy():
    meshes = os.path.join('OutputFolder/', 'meshes')
    CopyFiles('InputFolder()', meshes)