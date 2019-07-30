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
- [ ] edit two xml files at a time
- [ ] change string to `InputFolder`

## References used
- try, except for copy/paste - https://gist.github.com/keithweaver/562d3caa8650eefe7f84fa074e9ca949
- find and replace text - https://stackoverflow.com/questions/37868881/how-to-search-and-replace-text-in-an-xml-file-using-python?rq=1

## Consider
Create another version of this script which is a plugin instead