from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# 设置字体，如果没有，也可以不设置
font = ImageFont.truetype("STXINGKA.TTF", 60)  # 现在是宋体

# 打开底版图片,确定书写位置
imageFile = "2010619.jpg"
img = Image.open(imageFile)
# 在图片上添加文字
str1 = 'wei'
str2 = 'love'
width = img.width
height = img.height
print(width, height)
position1 = (width-60, height-60)
position2 = (width / 4, height / 5)
color = (255, 255, 0)
draw = ImageDraw.Draw(img)
draw.text(position1, str1, color, font=font)
draw.text(position2, str2, color, font=font)
# draw = ImageDraw.Draw(img)

# 保存图片
img.save("pp2.jpg")
print('运行结束')
