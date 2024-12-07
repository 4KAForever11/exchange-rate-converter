from cairosvg import svg2png
from PIL import Image
import io

# 先转换为PNG（多个尺寸）
sizes = [16, 32, 48, 64, 128, 256]
images = []

# 修改SVG内容，添加颜色
svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24"><g fill="none" stroke="#2196F3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><path d="M14.8 9A2 2 0 0 0 13 8h-2a2 2 0 0 0 0 4h2a2 2 0 0 1 0 4h-2a2 2 0 0 1-1.8-1"></path><path d="M12 6v2m0 8v2"></path></g></svg>'''

for size in sizes:
    png_data = svg2png(bytestring=svg_content.encode('utf-8'), 
                      output_width=size, 
                      output_height=size)
    image = Image.open(io.BytesIO(png_data))
    images.append(image)

# 保存为ICO
images[0].save('icon.ico', format='ICO', sizes=[(size, size) for size in sizes]) 