## Round one
- [x] user input folder to copy `InputFolder`
- [x] user input root folder to paste `OutputDirectory`

## Round two
- [x] Create a new folder in the `OutputRootFolder`
- [x] That folder needs to have the same name as the `InputFolder`

## Round three
- [x] create `meshes` subdirectory in `OutputFolder`
- [x] copy meshes from `InputFolder` into `meshes
- [ ] check try, except

## Round four
- [x] point to `SourceFolder` to use it for xml templates
- [x] copy templates from `SourceFolder` into `OutputFolder`

## Round five
- [x] edit sdf files
- [x] edit two xml files at a time
- [x] change string to `InputFolder`
- [x] figure out `__pycache__`

## References used
- try, except for copy/paste - https://gist.github.com/keithweaver/562d3caa8650eefe7f84fa074e9ca949
- find and replace text - https://stackoverflow.com/questions/37868881/how-to-search-and-replace-text-in-an-xml-file-using-python?rq=1
- tutorial: https://realpython.com/working-with-files-in-python/
- quick and easy os type references: https://www.bogotobogo.com/python/python_files.php
- Copy multiple files in Python: https://stackoverflow.com/questions/3397752/copy-multiple-files-in-python
- argparse things - https://stackoverflow.com/questions/51677207/argparse-input-and-output-directory
- creating nested directories - https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory

## Consider
Create another version of this script which is a plugin instead