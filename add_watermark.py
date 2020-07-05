from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# 设置字体，如果没有，也可以不设置
font = ImageFont.truetype('STXINGKA.TTF', 60)  # 现在是宋体

# 打开底版图片
imageFile = "2010619.jpg"
im1 = Image.open(imageFile)

# 在图片上添加文字 1
draw = ImageDraw.Draw(im1)
draw.text((0, 0), "love", (0, 0, 0), font=font)
draw = ImageDraw.Draw(im1)

# 保存
im1.save("pp.jpg")
print('运行结束')
