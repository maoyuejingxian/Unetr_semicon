################33data preprocessing##################33
import numpy as np
import os
import nibabel as nib
os.chdir("/home/maoyuejingxian/data_preprocess/Memory_preprocess/Groundtruth/")

fpath = os.getcwd()
path_list = os.listdir(fpath)
# print(path_list)
# print(fpath)
# img_path = "imagesTr/06s32_void_0000.nii.gz"
# img = nib.load(img_path)
# img_data = img.get_fdata()
# # print(img_data)
# print(img_data.shape)
# # print(np.unique(img_data))


def save_nifti(data,save_path):
    data_ = nib.load(save_path)
    header = data_.header
    nifti_image = nib.Nifti1Image(data,None,header)
    nib.save(nifti_image,"/home/maoyuejingxian/data_preprocess/Memory_preprocess/Groundtruth_changelabel/"+save_path)
    print('save file sucess')

for i in path_list:
    img = nib.load(i)
    img_data = img.get_fdata()
    A = img_data
    #for logic
    # A[(A>0.9)&(A<1.1)]=1
    # A[(A>2.9)&(A<3.1)]=2
    # A[(A>5.9)&(A<6.1)]=3
    # save_nifti(A,i)
####for memory

    A[(A>0.9)&(A<1.1)]=1
    A[(A>1.9)&(A<2.1)]=4
    A[(A>2.9)&(A<3.1)]=2
    A[(A>5.9)&(A<6.1)]=3
    
    save_nifti(A,i)

    # A[(A>0.9)&(A<1.1)]=1
    # A[(A>1.9)&(A<2.1)]=2
    # A[(A>2.9)&(A<3.1)]=3
    # A[(A>5.9)&(A<6.1)]=4
    # save_nifti(A,i)



