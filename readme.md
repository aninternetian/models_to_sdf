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

2. Creates SDF templates based on the folder and model names
- Copies existing sdf from the script
- edits the sdf to the name of the folder and models

## How to use - Linux
Make sure your models and textures have the same name as the folder name and make sure the folder doesn't exist in the output directory.

1. Open a terminal from the `models_to_sdf/` directory
2. Type in `python3 models_to_sdf.py`
3. Type in the `--input` directory where the models and textures are exported. Eg: `~/Documents/models/robots/sesto`
4. Type out the `--output` directory where the gazebo models are exported. Eg: `~/Dropbox/models/`

Your line should look something like this:
```
python3 models_to_sdf.py --input ~/Documents/models/robots/sesto --output ~/Dropbox/models/
```

## How to use - Windows

1. Open a terminal from the `models_to_sdf\` directory
2. Run `py -3 models_to_sdf.py`
3. Type in the `--input` directory where the models and textures are exported. Eg: `C:\Documents\models\robots\sesto`
4. Type out the `--output` directory where the gazebo models are exported. Eg: `C:\Dropbox\models`
```
py -3 models_to_sdf.py --input C:\Documents\models\robots\sesto --output C:\Dropbox\models

```
In case you come across any issues - https://stackoverflow.com/a/26616078

## To-dos
- clean it up
- get it to check if the folder exists or not
