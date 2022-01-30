import pydicom as dicom
import matplotlib.pylab as plt
image_path = 'C:/Users/Samarth Mahendra/Downloads/HHT_CINE_Segmented_SAX_b1-20220117T170613Z-001\HHT_CINE_Segmented_SAX_b1/image_02.dcm'
ds = dicom.dcmread(image_path)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)