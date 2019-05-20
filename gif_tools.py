# -*- coding: utf-8 -*-
#python3.7+
#2019/5/20 GIF快速制作工具（未完成）

__author__='gamefang'

#pip install pillow
from PIL import Image

def make_gif(files,dur=0.2):
    '''
    序列帧图片迅速变gif
    @param files: 帧图片文件
    @param dur: gif图播放间隔秒数
    '''
    imgs = []
    for file in files:
        imgs.append(Image.open(file))
    imgs[0].save('test.gif',save_all=True,loop=True,append_images=imgs,duration=dur)

def split_gif(file):
    '''
    拆解gif图片
    '''
    im = Image.open(file)
    n = 0
    mypalette =  im.getpalette()
    try:
        im.putpalette(mypalette)
        new_im = Image.new('RGBA',im.size)
        new_im.paste(im)
        new_im.save('split/%s.png' % n)
        n += 1
        im.seek(im.tell() +1)
    except EOFError:
        pass
    
if __name__ == '__main__':
    FPATHS = [r'1.png',r'2.png',r'3.png']
    make_gif(FPATHS)
    split_gif('test.gif')
