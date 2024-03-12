import cv2
import numpy as np

def calculate_black_white_ratio(img):
    black_pixels = 0
    white_pixels = 0
    trashcan_started = False

    # 获取图像高度和宽度
    height, width = img.shape[:2]

    for i in range(height):
        for j in range(width):
            pixel_value = img[i, j]

            if pixel_value != 0:
                white_pixels += 1
                trashcan_started = False
            elif not trashcan_started:
                black_pixels += 1
            else:
                break

    # 计算黑白像素的比例
    total_pixels = black_pixels + white_pixels
    black_white_ratio = black_pixels / total_pixels, white_pixels / total_pixels

    return black_white_ratio

# 示例用法
image_path = 'sample_images/BWRC.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is not None:
    result = calculate_black_white_ratio(img)
    print(f"黑色像素占比: {result[0]:.2%}, 白色像素占比: {result[1]:.2%}")
else:
    print("无法读取图片，请检查路径是否正确。")
