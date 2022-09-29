#!/usr/bin/env python
# coding: utf-8

# In[1]:




#import os
import sys
sys.path.append('/home/fernando/Downloads/TESIS-DOUTORADO-2/PESQUISA/libraries/OpenPifPafTools/src');
sys.path.append('../src');

import VideoImageTools as vit
import openpifpaf
import OpenPifPafTools.OpenPifPafAnnotations as oppt
import matplotlib.pyplot as plt

import cv2
import numpy as np
from PIL import Image


# In[ ]:


vin_path ='/mnt/boveda/DATASETs/DANCE-VIDEOS/dance1_mini.mp4';
vout_path='/mnt/boveda/DATASETs/DANCE-VIDEOS/output_borrame_dance1.mp4';



def my_func(predictor,frame):
    img_tmp = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);
    pil_im = Image.fromarray(img_tmp);
    
    predictions, gt_anns, image_meta = predictor.pil_image(pil_im);
    
    img_pil_tmp=oppt.write_openpifpaf_annotation_in_pil_img(pil_im,predictions,method='temporal_file');
    
    frame_rgb=np.asarray(img_pil_tmp);
    
    frame=cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR) # the color is converted from RGB to BGR format
    
    return frame;

predictor = openpifpaf.Predictor(checkpoint='shufflenetv2k16')#'shufflenetv2k16-wholebody
vit.apply_func_predictor_over_video_outmp4(my_func,predictor,vin_path,vout_path)

print('working end')


# In[ ]:




