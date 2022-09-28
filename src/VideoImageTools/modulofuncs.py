#!/usr/bin/python

import numpy as np
import cv2
from tqdm.notebook import tqdm

def apply_func_predictor_over_video_outmp4(func,predictor,vin_path,vout_path,show=False):
    
    fps=25;
    
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    
    # capture
    cap = cv2.VideoCapture(vin_path);

    if int(major_ver)  < 3 :
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    else :
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter(vout_path, fourcc, fps, (width,height))
    
    
    with tqdm(total=total_frames, desc="Working", bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
        while(cap.isOpened()):
            ret, frame = cap.read()
            pbar.update(1);
            
            if ret==True:
                #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                frame=func(predictor,frame);
                
                out.write(frame);

                if show==True:
                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            else:
                break;


    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return True;


