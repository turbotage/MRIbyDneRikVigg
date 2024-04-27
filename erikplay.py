import numpy as np
import ants
import napari
import os

datanat = os.path.join(os.getcwd(), 'data_anat/')

pdimg = ants.image_read(os.path.join(datanat, 'sub-01_PDmap.nii.gz')).numpy()
r1img = ants.image_read(os.path.join(datanat, 'sub-01_R1map.nii.gz')).numpy()
r2img = ants.image_read(os.path.join(datanat, 'sub-01_R2starmap.nii.gz')).numpy()

#viewer = napari.Viewer()
#viewer.add_image(pdimg, name='PDmap')
#viewer.add_image(r1img, name='R1map')
#viewer.add_image(r2img, name='R2map')
#viewer.show(block=True)


# PD ~ Proton Density = True proton density * camera gain
# R1 = 1 / T1
# R2* = 1 / T2*

# Gradient Echo Signal equation

# S = PD * sin(alpha) * exp(-TE/T2*) * (1 - exp(-TR/T1)) / (1 - cos(alpha) * exp(-TR/T1))

# Machine settable
# alpha
# TE
# TR

TR = 0.008
TE = 0.002
alpha = 30 * np.pi / 180

r2img[r2img < 0] = 0

#viewer = napari.Viewer()
#viewer.show(block=True)

E1 = np.exp(-TR * r1img)
E2 = np.exp(-TE * r2img)
SI = np.sin(alpha) * E2 * (1 - E1) / (1 - np.cos(alpha) * E1)

viewer = napari.Viewer()
#viewer.add_image(0 / r2img, name='T2*')
#viewer.add_image(0 / r1img, name='T1')
viewer.add_image(SI, name=f'SI TR={TR} TE={TE} alpha={alpha}')
viewer.show(block=True)
