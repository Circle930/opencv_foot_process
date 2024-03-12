import cv2
import numpy as np

def calculate_black_white_ratio(img):

    # 计算黑色和白色像素的数量
    total_pixels = img.size
    black_pixels = np.sum(img == 0)
    white_pixels = total_pixels - black_pixels

    # 计算黑白像素的比例
    black_white_ratio = black_pixels / total_pixels, white_pixels / total_pixels

    return black_white_ratio

# # 示例用法
# image_path = 'sample_images/LL.jpg'
# image = cv2.imread(image_path)

# if image is not None:
#     # 计算黑白像素的比例
#     black_ratio, white_ratio = calculate_black_white_ratio(image)
#     print(f"黑色像素占比: {black_ratio:.2%}")
#     print(f"白色像素占比: {white_ratio:.2%}")
# else:
#     print("无法读取图片，请检查路径是否正确。")