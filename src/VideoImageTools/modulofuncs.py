#!/usr/bin/python

import numpy as np
import cv2

import VideoImageTools as vit


if vit.in_ipynb():
    from tqdm.notebook import tqdm
    #print("notebook")
else:
    from tqdm import tqdm
    #print("console")

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
    #with tqdm(range(total_frames)) as pbar:
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


def apply_func_predictor_over_video_to_frames(func, predictor, vin_path, vout_dir, show=False,FORMATO = "frame_{:05d}.png"):
    # Cria a pasta de saída se não existir
    if not os.path.exists(vout_dir):
        os.makedirs(vout_dir)
    
    # Captura de vídeo
    cap = cv2.VideoCapture(vin_path)
    
    # Verifica a versão do OpenCV
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(major_ver) < 3:
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    else:
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Salva o FPS em um arquivo JSON
    json_data = {'fps': fps}
    json_filename = os.path.join(vout_dir, 'video_info.json')
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
   
    # Loop pelos frames do vídeo
    with tqdm(total=total_frames, desc="Processing", bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            pbar.update(1)
            
            if ret:
                # Aplica a função ao frame
                processed_frame = func(predictor, frame)
                
                # Formata o nome do arquivo
                frame_filename = os.path.join(vout_dir, FORMATO.format(frame_count))
                
                # Salva o frame processado na pasta de saída
                cv2.imwrite(frame_filename, processed_frame)
                
                frame_count += 1

                if show:
                    cv2.imshow('Frame', processed_frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            else:
                break

    cap.release()
    cv2.destroyAllWindows()
    return True


