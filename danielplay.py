import numpy as np
import ants
import napari
import os

from matplotlib import pyplot as plt

# Data folder
datanat = os.path.join(os.getcwd(), 'data_anat/')

# PD, R1, R2* imgs
pdimg = ants.image_read(os.path.join(datanat, 'sub-01_PDmap.nii.gz'))
r1img = ants.image_read(os.path.join(datanat, 'sub-01_R1map.nii.gz'))
r2img = ants.image_read(os.path.join(datanat, 'sub-01_R2starmap.nii.gz'))

# Settable constants
TR = 0.008
TE = 0.002
alpha = 15*np.pi/180


#### MOTHER EQUALRTIOTIOTION!!!! ######
# S = PD * sin(alpha) * exp(-TE/T2) * (1 - exp(-TR/T1)) / (1 - cos(alpha) * exp(-TR/T1))

pd_mat = pdimg.numpy()
r1_mat = r1img.numpy()
r2_mat = r2img.numpy()

r2_mat[r2_mat<0] = 0

max_val = max(pd_mat.max(), r1_mat.max(), r2_mat.max())

pd_mat /= max_val
r1_mat /= max_val
r2_mat /= max_val

ER1 = np.exp(-TR*r1_mat)
ER2 = np.exp(-TE*r2_mat)

S = pd_mat * np.sin(alpha) * ER2 * (1 - ER1) / (1 - np.cos(alpha)*ER1)

S_lims = np.percentile(S, (2.5, 97.5))
S[S < S_lims[0]] = S_lims[0]
S[S > S_lims[1]] = S_lims[1]

viewer = napari.Viewer()
#viewer.add_image(pd_mat, name='PDmap')
#viewer.add_image(r1_mat, name='R1map')
#viewer.add_image(r2_mat, name='R2map')
viewer.add_image(S, name='Smap')
viewer.show(block=True)





