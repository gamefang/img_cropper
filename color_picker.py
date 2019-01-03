# -*- coding: utf-8 -*-
#python3.7+
#2019/1/3 按块取色工具

__author__='gamefang'
version='v1.0.5'

#pip install pillow
from PIL import Image

def color_convert(value,export_str=False):
    '''
    RGB/十六进制互转
    @param value: RGB元组或十六进制色字符串
    @param export_str: 选择导出字符串型/数值型的十六进制色
    @return: 相反类型的值
    '''
    digit = list(map(str, range(10))) + list("ABCDEF")
    if isinstance(value, tuple):
        string = '#'
        for i in value:
            a1 = i // 16
            a2 = i % 16
            string += digit[a1] + digit[a2]
        if export_str:
            return string
        else:
            return int(string.replace('#','0x'),base=16)
    elif isinstance(value, str):
        a1 = digit.index(value[1]) * 16 + digit.index(value[2])
        a2 = digit.index(value[3]) * 16 + digit.index(value[4])
        a3 = digit.index(value[5]) * 16 + digit.index(value[6])
        return (a1, a2, a3)

def color_picker(img,tile_w,tile_h,use_rgb=True):
    '''
    获取图片所有取色点色值，按从左到右从上到下优先级
    @param img: Image对象
    @tile_w: 待切割的图块宽
    @tile_h: 待切割的图块高
    @use_rgb: 使用RGB颜色/使用十六进制色
    @return: 取色点的颜色值列表
    '''
    width,height = img.size
    colors = []
    for point_y in range( height // tile_h + 1 ):
        for point_x in range( width // tile_w + 1 ):
            this_point = (point_x * tile_w , point_y * tile_h)
            this_color = img.getpixel(this_point)[:3]   #忽略png的alpha
            print(this_point,this_color)
            if not use_rgb:this_color=color_convert(this_color)
            colors.append( this_color )
    return colors
        
if __name__ == '__main__':
    FPATH = r'C:\Users\ran\Desktop\timg.jpg'
    FPATH = r'C:\Users\ran\Desktop\weapon_tex.png'
    img = Image.open(FPATH)
    colors = color_picker(img,64,64,False)
    print(colors)
