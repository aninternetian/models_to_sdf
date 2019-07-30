import os

input = '~/Documents/Prev/hospital/beds/CGMClassic'
output = '~/Documents/work/test/'

inputFolderName = os.path.basename(input)

sdfDir = os.path.join(output, inputFolderName)
print(sdfDir)