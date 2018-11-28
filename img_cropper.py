# -*- coding: utf-8 -*-
#python3.6+
#2018/11/22 可定制的图片切割器

__author__='gamefang'
version='v1.0.5'

import os

#pip install pillow
from PIL import Image

#加载配置并全局化
import configparser
cfg=configparser.ConfigParser()
cfg.read('img_cropper.ini',encoding='utf8')
cfg={ **cfg._defaults,**cfg._sections }

def image_split(fpath, rownum, colnum, dstpath='',keepempty=False):
    '''
    将整张图片均匀切割成若干张小图片
    @param fpath: 图片文件的完整路径
    @param rownum: 准备切割的行数
    @param colnum: 准备切割的列数
    @param dstpath: 切割后图片保存的完整路径，留空则使用/crop
    @param keepempty: 输出没有内容的空图片
    '''   
    img = Image.open(fpath)
    w, h = img.size
    if 1 <= rownum <= h and 1 <= colnum <= w:
        print(f'开始切割 {fpath} ( {w}x{h}, {img.format}, {img.mode} )')
        paths = os.path.split(fpath)
        fn = paths[1].split('.')
        basename = fn[0]
        ext = fn[-1]
        if not dstpath:
            dstpath=paths[0] + f'/{basename}'
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)
        count = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                cropped_img=img.crop(box)
                if keepempty or cropped_img.getbbox():
                    cropped_img.save(os.path.join(dstpath, f'{basename}_{count}.{ext}'), ext)
                else:
                    print(f'    第{count}张图片没有元素，不输出！')
                count += 1
        print(f'图片切割至 {dstpath} ，共生成 {count} 张小图片。')
    else:
        print(f'{fpath}行列切割参数有问题！')
    
def main(cfg):
    for fn,info in cfg['tasks'].items():
        rownum,colnum,*others=info.split(',')
        input_path=os.path.join(cfg['input_path'],fn)
        input_path=os.path.abspath(input_path)
        if cfg['output_path']:
            output_path=os.path.abspath(cfg['output_path'])
        else:
            output_path=''
        image_split(input_path,int(rownum),int(colnum),output_path)
        
if __name__ == '__main__':
   main(cfg)
