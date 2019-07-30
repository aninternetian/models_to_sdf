import os
import editSdf

input = '/home/roselle/Documents/Prev/hospital/beds/CGMClassic/'
output = '/home/roselle/Documents/work/test/CGMClassic/'

inputFolderName = os.path.basename(input)
sdfDir = os.path.join(output, inputFolderName)

sdfPath = os.path.join(sdfDir, 'model.sdf')
editSdf.replaceValue(sdfPath)