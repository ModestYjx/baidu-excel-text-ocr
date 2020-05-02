# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Tue Jun 12 09:37:38 2018
# 利用百度api实现图片文本识别
# @author: XnCSD
# """
#
# import glob
# from os import path
# import os
# import shutil
# import os
# from aip import AipOcr
# from PIL import Image
# import win32clipboard as w
# import win32con
# from PIL import ImageGrab
# import numpy as np
# import time
#
#
#
# def convertimg(picfile, outdir):
#     '''调整图片大小，对于过大的图片进行压缩
#     picfile:    图片路径
#     outdir：    图片输出路径
#     '''
#     img = Image.open(picfile)
#     width, height = img.size
#     while (width * height > 4000000):  # 该数值压缩后的图片大约 两百多k
#         width = width // 2
#         height = height // 2
#     new_img = img.resize((width, height), Image.BILINEAR)
#     new_img.save(path.join(outdir, os.path.basename(picfile)))
#
#
# def baiduOCR(picfile, outfile):
#     """利用百度api识别文本，并保存提取的文字
#     picfile:    图片文件名
#     outfile:    输出文件
#     """
#     filename = path.basename(picfile)
#
#     APP_ID = '****'  # 刚才获取的 ID，下同
#     API_KEY = '****'
#     SECRECT_KEY = '****'
#     client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
#
#     i = open(picfile, 'rb')
#     img = i.read()
#     print("正在识别图片：\t" + filename)
#     # message = client.basicGeneral(img)  # 通用文字识别，每天 50 000 次免费
#     message = client.basicAccurate(img)   # 通用文字高精度识别，每天 800 次免费
#     print("识别成功！")
#     i.close();
#
#     with open(outfile, 'a+') as fo:
#         # fo.writelines("+" * 60 + '\n')
#         # fo.writelines("识别图片：\t" + filename + "\n" * 2)
#         fo.writelines("文本内容：\n")
#         # 输出文本内容
#         print(message.get('words_result'))
#         for text in message.get('words_result'):
#             fo.writelines(text.get('words') + '\n')
#         fo.writelines('\n' * 2)
#     print("文本导出成功！")
#     print()
#
#
#
# def CleanDir( Dir ):
#     if os.path.isdir( Dir ):
#         paths = os.listdir( Dir )
#         for path in paths:
#             filePath = os.path.join( Dir, path )
#             if os.path.isfile( filePath ):
#                 # try:
#                 os.remove( filePath )
#                 # except os.error:
#                 #     # autoRun.exception( "remove %s error." %filePath )#引入logging
#             elif os.path.isdir( filePath ):
#                 if filePath[-4:].lower() == ".svn".lower():
#                     continue
#                 shutil.rmtree(filePath,True)
#     return True
#
#
#
# if __name__ == "__main__":
#
#     outfile = 'export.txt'
#     outdir = 'compressDir'
#     imgName = 'ocrImg.png'
#     if path.exists(outfile):
#         os.remove(outfile)
#     if not path.exists(outdir):
#         os.mkdir(outdir)
#
#     # for picfile in glob.glob("picture/*"):
#     picfile = ImageGrab.grabclipboard() # 获取剪贴板文件
#     if isinstance(picfile, Image.Image):
#         print("Image: size : %s, mode: %s" % (picfile.size, picfile.mode))
#         picfile.save(imgName)
#         print("压缩过大的图片...")
#         # // 首先对过大的图片进行压缩，以提高识别速度，将压缩的图片保存与临时文件夹中
#         for picfile in glob.glob(imgName):
#             convertimg(picfile, outdir)
#         print("图片识别...")
#         for picfile in glob.glob(imgName):
#             baiduOCR(picfile, outfile)
#             os.remove(picfile)
#         print('图片文本提取结束！文本输出结果位于 %s 文件中。' % outfile)
#         os.system(r'notepad export.txt')
#         # os.remove(pictr)
#         CleanDir(outdir)
#         os.removedirs(outdir)
#
#     else:
#          print("剪切板无图片")
#          pass
#
#
#
