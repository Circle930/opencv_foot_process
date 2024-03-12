import cv2
import numpy as np
from matplotlib import pyplot as plt

def detect_foot_direction(img):
    
    # 读取图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 使用Canny边缘检测
    edges = cv2.Canny(gray, 110, 150, apertureSize=3)
    
    # 寻找轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历轮廓
    for contour in contours:
        # 计算轮廓的边界框
        x, y, w, h = cv2.boundingRect(contour)

        # 判断是否为长条型镂空区域，可根据实际情况调整阈值
        if w > 5 * h:
            # 镂空朝上，无需处理
            # print("镂空朝上")
            return "Front", img, edges  # 返回方向、原图和边缘

        # 镂空朝下，需要旋转图像，获取图像的高度和宽度
        height, width = img.shape[:2]

        # 设置旋转中心点
        center = (width // 2, height // 2)

        # 设置旋转角度为180度
        angle = 180

        # 计算旋转矩阵
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

        # 进行旋转
        rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))
        print("镂空朝下，已旋转图像")

        # 判断左右
        center_x = x + w // 2
        img_center_x = img.shape[1] // 2

        if center_x < img_center_x:
            return "Left", rotated_img, edges
        else:
            return "Right", rotated_img, edges

    print("未找到合适的镂空区域")
    return "Undetermined", img, edges  # 返回方向、原图和边缘

# # 测试
# img_path = 'sample_images/LL.jpg'
# direction, result_img, edges = detect_foot_direction(img_path)

# # 显示处理后的图像和边缘
# if isinstance(result_img, np.ndarray):
#     plt.subplot(121), plt.imshow(result_img, cmap='gray')
#     plt.title('Result Image'), plt.xticks([]), plt.yticks([])

#     plt.subplot(122), plt.imshow(edges, cmap='gray')
#     plt.title('Canny Edges'), plt.xticks([]), plt.yticks([])

#     plt.show()

# print("脚掌位置:", direction)
