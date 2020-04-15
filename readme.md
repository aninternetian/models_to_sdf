## What this setup will do

Folder structure based on the SDF requirements for the [Model Database Structure](http://gazebosim.org/tutorials?tut=model_structure&cat=build_robot)

1. Manipulate folders:
- copies contents from the original folder into the specified folder
- move the contents into a created "meshes" folder

2. Creates SDF templates based on the folder and model names
- Copies existing sdf from the script
- Edits the sdf to the name of the folder and models

## Recommended export settings
- Export using Y forward, Z up in Blender.
- The "front" of the object is the side which gets interacted with robots. (Ie, handles of the wheelchair is to face the +X direction in Gazebo)
- Make sure your "front" side of the object is facing the +X direction/forward.

## Before using Example

Artist exports models with textures into one folder

Folder contents:
- Model base meshes (supports .obj only)
- Model joints/wheels or parts meshes
- Collision model meshes (low poly)
- Model textures (recommended to use .png)

Example folder might look like this:

Sesto
- Sesto.obj
- Sesto.mtl
- Sesto_Col.obj
- Sesto_Col.mtl
- SestoWheel.obj
- SestoWheel.mtl
- SestoWheel_Col.obj
- SestoWheel_Col.mtl
- Sesto_Diffuse.png, etc

Take note of the above:
- Model and folder has the same name.
- Collision model has a `_Col` at the end of the name.

## How to use - Linux
Make sure this folder doesn't exist in the output directory.

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
