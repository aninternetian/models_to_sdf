import editSdf
import os

input = '~/models_to_sdf/templates'
output = '/home/roselle/Documents/work/test/

inputFolderName = os.path.basename(input)

sdfDir = os.path.join(output, inputFolderName)

sdfPath = os.path.join(sdfDir, 'model.sdf')
editSdf.replaceValue(sdfPath)

#configPath = os.path.join(sdfDir, 'model.config')
#editSdf.replaceValue(configPath)