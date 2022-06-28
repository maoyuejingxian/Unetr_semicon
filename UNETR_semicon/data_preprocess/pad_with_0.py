#####pad inmage with 0
#notice: padding should be performed on raw data, Groundtruth_changelabel
import torch.nn.functional as f
import torch
import numpy as np
import os
import nibabel as nib

os.chdir("/home/maoyuejingxian/data_preprocess/Logic_preprocess/Groundtruth_changelabel/")
fpath = os.getcwd()
path_list = os.listdir(fpath)
# print(path_list)

# img_path = "zdb_logic_d1_b2_s7_126_void.nii.gz"
# img = nib.load(img_path)
# img_data = img.get_fdata()
# print(img_data.shape)
# x = torch.Tensor(img_data)
# print(x.shape)
# # pad_dim = (7,7,2,1,9,9)#how to get pad_dim for each image?
# x = f.pad(x,pad_dim,"constant")
# print(x.shape)
# print(type(pad_dim))

def get_pad_dim(img_shape):
    pad_dim_list = []
    x = img_shape[0]
    y = img_shape[1]
    z = img_shape[2]
    minus_z = 96-z
    minus_y = 96-y
    minus_x = 96-x
    # if minus_z%2 == 0:
    #     z1 = minus_z//2
    #     z2 = minus_z//2
    # else:
    #     z1 = 0
    #     z2 = 0
    #     while z1+z2!=minus_z:
    #         z_ = np.random.randint(minus_z,size=2)
    #         z1=z_[0]
    #         z2=z_[1]
    z1 = minus_z//2
    z2 = minus_z-z1
    pad_dim_list.append(z1)
    pad_dim_list.append(z2)

    # if minus_y%2 == 0:
    #     y1 = minus_y//2
    #     y2 = minus_y//2
    # else:
    #     y1 = 0
    #     y2 = 0
    #     while y1+y2!=minus_y:
    #         y_ = np.random.randint(minus_y,size=2)
    #         y1=y_[0]
    #         y2=y_[1]
    y1 = minus_y//2
    y2 = minus_y-y1
    pad_dim_list.append(y1)
    pad_dim_list.append(y2)

    # if minus_x%2 == 0:
    #     x1 = minus_x//2
    #     x2 = minus_x//2
    # else:
    #     x1 = 0
    #     x2 = 0
    #     while x1+x2!=minus_x:
    #         x_ = np.random.randint(minus_x,size=2)
    #         x1=x_[0]
            # x2=x_[1]
    x1 = minus_x//2
    x2 = minus_x-x1
    pad_dim_list.append(x1)
    pad_dim_list.append(x2)
    pad_dim = tuple(pad_dim_list)
    return pad_dim
# shape = x.shape

# s = get_pad_dim(shape)
# print(s)
# x = f.pad(x,s,"constant")
# print(x.shape)
# print(type(pad_dim))

def pad_0(dim,tensor_data):
    img_pad_0 = f.pad(tensor_data,dim,"constant")
    return img_pad_0

def save_nifti(data,save_path):
    data_ = nib.load(save_path)
    header = data_.header
    nifti_image = nib.Nifti1Image(data,None,header)
    nib.save(nifti_image,"/home/maoyuejingxian/data_preprocess/Logic_preprocess/Groundtruth_pad0/"+save_path)
    print('save file sucess')

for i in path_list:
    img = nib.load(i)
    img_data = img.get_fdata()
    img_tensor = torch.Tensor(img_data)
    shape = img_data.shape
    d = get_pad_dim(shape)
    final_img = pad_0(d,img_tensor)
    print(final_img.shape)
    save_nifti(final_img,i)



# z1 = 0
# z2 = 0
# while z1+z2!=9:
#     z_ = np.random.randint(9,size=2)
#     z1=z_[0]
#     z2=z_[1]

# print(z1)
# print(z2)


