# _*_  coding:utf-8 _*_
import os
from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from azat import ROOT_DIR
#设置字体，如果没有，也可以不设置
# font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf",13)

#打开底版图片
BASE_URL =os.getcwd()
def typeWords(name,id_num,key_num):
# def type():
    muban = os.path.join(ROOT_DIR,'static/image/certificate.png')
    #导入需要修改的图片
    image = Image.open(muban)
    # target=image.copy()
    # 设置字体的字体和大小
    font_src = os.path.join(BASE_URL,'static/font/font.ttf')
    font = ImageFont.truetype(font_src, 80)
    fontk = ImageFont.truetype(font_src, 100)
    font_d = ImageFont.truetype(font_src, 50)
    # 调用Draw方法,传入导入图片对象
    draw = ImageDraw.Draw(image)
    msg=name
    id_num = id_num
    key_num = key_num
    key ="授权编号 : %s"%key_num
    date =datetime.now().strftime(' 20%y 年 %m 月 %d 日 ')
    # key = "0210230651"
    w, h = draw.textsize(msg.encode('utf-8'))
    wi, hi = draw.textsize(id_num.encode('utf-8'))
    wk, hk = draw.textsize(key.encode('utf-8'))
    wd, hd = draw.textsize(key.encode('utf-8'))
    W, H= image.size
    # target = Image.new("RGBA", (W, H), "yellow")
    # target.save(os.path.join(BASE_URL,'static/image/generated/%s.png'%key_num))
    draw.text(((W-w)/3.5,(H-h)/2.8), msg, fill='black', font=font)
    draw.text(((W-wi)/3.5,(H-hi)/2.5), id_num, fill='black', font=font)
    draw.text(((W-wk)/3.2,(H-hk)/1.5), key, fill='black', font=fontk)
    draw.text(((W-wd)/2.4,(H-hd)/1.22), date, fill='black', font=font_d)
    # draw.text方法是用来在图片上加上文字
    # draw.text((x, y), '5', fill=(255, 10, 10), font=font)
    # (x,y)是一个元组用来表示生成的位置,x表x轴的位置,y表示在y轴的位置
    # 需要注意的是:坐标轴的原点是图片的左上角
    # '5' 表示的是需要在图片上写入的文字
    # fill=(255, 10, 10) 表示的是RGB的色值
    # font=font 表示字体,传入定义好的字体
    # './images/change.png''./images/'保存的图片路径,../change.png需要保存的图片名
    # 'png' 图片保存的格式
    # target = os.path.join(BASE_URL,"static/image/generated/%s.png"%key_num)
    # target = "%s/static/images/certificates/%s.png"%(BASE_URL,key_num)
    # target = Image.new("RGB", (128, 128), "#FF0000")
    # target.save(os.path.join(BASE_URL,"static/image/generated/%s.png"%key_num))
    # base=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))))
    base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # base=os.getcwd()
    target = os.path.join(base,'static/image/certificates')
    # image.save(os.path.join('%s.png'%key_num),'png')
    image.save(os.path.join(target,'%s.png'%key_num))
    # image.save("static/image/certificates/%s.png"%key_num)
    return os.path.join(target,'%s.png'%key_num)

# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print()