## Example

Artist exports models with textures

Folder name: "HospitalModel"
Folder contents:
- model.dae or model.obj
- model.jpg or model.png

## What this setup will do

1. Manipulate folders:
- copies the contents into the specified folder
- move the contents into a created "meshes" folder
- creates the sdf files based on the folder name

2. Edits the sdf files:
- model.config
- model.sdf

## How to use
1. Change to directory `models_to_sdf/` 
2. Run `models_to_sdf.py`