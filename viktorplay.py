import numpy as np
import ants
import napari
import os

datanat = os.path.join(os.getcwd(), 'data_anat/')

pdimg = ants.image_read(os.path.join(datanat, 'sub-01_PDmap.nii.gz'))
r1img = ants.image_read(os.path.join(datanat, 'sub-01_R1map.nii.gz'))
r2img = ants.image_read(os.path.join(datanat, 'sub-01_R2starmap.nii.gz'))

viewer = napari.Viewer()
viewer.add_image(pdimg.numpy(), name='PDmap')
viewer.add_image(r1img.numpy(), name='R1map')
viewer.add_image(r2img.numpy(), name='R2map')
viewer.show(block=True)

