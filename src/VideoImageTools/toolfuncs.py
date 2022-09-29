import numpy as np
from PIL import Image

def in_ipynb():
    try:
        cfg = get_ipython().config 
        if cfg['IPKernelApp']['parent_appname'] == 'ipython-notebook':
            return True
        else:
            return False
    except NameError:
        return False


def fig_to_3ch_nparray(fig, show=True):
    '''
    Convert a fig in to a 3 channel numpy array.
    
    :param fig: figure returned by matplotlib.
    :type fig: matplotlib.figure.Figure
    :param show: Enable `fig.canvas.draw()`, need to draw if figure is not drawn yet.
    :type show: bool
    :return: A 3D numpy array (RGB image with 3 channel).
    :rtype: numpy.array
    '''
    if show:
        fig.canvas.draw()
    
    rgba_buf = fig.canvas.buffer_rgba()
    (w,h) = fig.canvas.get_width_height()
    rgba_arr = np.frombuffer(rgba_buf, dtype=np.uint8).reshape((h,w,4))
    
    return rgba_arr[:,:,0:3];
    

def fig_to_3ch_pil(fig, show=True):
    '''
    Convert a fig in to a 3 channel pil image.
    
    :param fig: figure returned by matplotlib.
    :type fig: matplotlib.figure.Figure
    :param show: Enable `fig.canvas.draw()`, need to draw if figure is not drawn yet.
    :type show: bool
    :return: A pil RGB image (with 3 channels).
    :rtype: PIL
    '''
    
    img_numpy=fig_to_3ch_nparray(fig,show=show);
    img_pil=Image.fromarray(img_numpy);
    
    return img_pil;
