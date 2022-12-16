import os
import numpy as np
import os.path as osp
import mmcv
import matplotlib.pyplot as plt
data = np.array([[1,2,3],[4,5,6]])
print(data.shape)
print(np.where(data==3))
data[np.where(data==3)] = 0
print(data)
print(osp.splitext('test.py'))
print(os.listdir('./'))
class TestDemo():
    def __init__(self, brightness: float=None,contrast: float=None,saturation: float=None,hue: float=None):
        self.brightness = brightness
        self.contrast = contrast
        self.saturation = saturation
        self.hue = hue
        print(eval('brightness'))
        color_params = ['contrast','brightness','saturation','hue']
        self.color_params = {}
        for param in color_params:
            if eval(param) is not None:
                self.color_params.update({param:eval(param)})
            print(param,type(eval(param)))
        # print([eval(param) for param in color_params])
        # self.color_params = dict([(param,eval(param)) for param in color_params if eval(param) is not None])
        print(self.color_params)
demo = TestDemo()
img_dir = '../mmsegmentation/data/REFUGE/annotations/test'
#training:(2056, 2124, 3),validation:(1634, 1634, 3),test:(1634, 1634, 3)
files = os.listdir(img_dir)
for file in files:
    path = osp.join(img_dir,file)
    img = mmcv.imread(path)
    if img.shape != (2056, 2124, 3):
        print(img.shape)
    # assert img.shape == (2056, 2124, 3)
    # print('shape:',img.shape)
    # img = img*127
    # plt.imshow(img,cmap='gray')
    # plt.show()
