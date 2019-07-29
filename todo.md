## First round
- [x] user input folder to copy `InputFolder`
- [x] user input root folder to paste `OutputRootFolder`

## Second round
- [ ] Create a new folder in the `OutputRootFolder`
- [ ] That folder needs to have the same name as the `InputFolder`

## Third round
- [ ] create `meshes` subdirectory in `OutputFolder`
- [ ] copy meshes from `InputFolder` into `meshes`

## Last round
- [ ] point to `SourceFolder` to use it for xml templates
- [ ] copy templates from `SourceFolder` into `OutputFolder`
- [ ] edit sdf files using name of the `InputFolder`

## References used
- tutorial: https://realpython.com/working-with-files-in-python/
- quick and easy os type references: https://www.bogotobogo.com/python/python_files.php
- Copy multiple files in Python: https://stackoverflow.com/questions/3397752/copy-multiple-files-in-python
- argparse things - https://stackoverflow.com/questions/51677207/argparse-input-and-output-directory