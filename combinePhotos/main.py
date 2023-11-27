'''
Description: Copyright (c) ydfk. All rights reserved
Author: ydfk
Date: 2023-11-27 14:25:03
LastEditors: ydfk
LastEditTime: 2023-11-27 14:30:17
'''
from PIL import Image

# 打开两张图片
image1 = Image.open('C:/Users/liyuhang/Desktop/a.PNG')
image2 = Image.open('C:/Users/liyuhang/Desktop/b.PNG')

# 调整图片尺寸
a4_width, a4_height = 2480, 3508  # A4纸张的尺寸，单位为像素
image1 = image1.resize((a4_width, a4_height // 2))
image2 = image2.resize((a4_width, a4_height // 2))

# 合并图片
result = Image.new('RGB', (a4_width, a4_height))
result.paste(image1, (0, 0))
result.paste(image2, (0, a4_height // 2))

# 保存合并后的图片
result.save('C:/Users/liyuhang/Desktop/output.jpg')
