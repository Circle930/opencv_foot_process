import cv2
import numpy as np

def crop_plastic_board(img_path):
   
    # 读取图片
    img = cv2.imread(img_path)

    # 将图片转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 对图像进行模糊处理，以便更好地找到轮廓
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)

    # 使用Canny边缘检测找到边缘
    edges = cv2.Canny(blurred, 100, 150)

    # 找到轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找到最大的轮廓
    max_contour = max(contours, key=cv2.contourArea)

    # 获取最小外接矩形
    x, y, w, h = cv2.boundingRect(max_contour)

    # 截取边界框
    cropped_image = img[y:y+h, x:x+w]

    return cropped_image

# # 调用测试
# img_path = 'sample_images/LL.jpg' # 替换成你的图片文件路径
# result_image = crop_plastic_board(img_path)

# # 显示原始图片和截取的图片
# cv2.imshow('Original Image', cv2.imread(img_path))
# cv2.imshow('Cropped Image', result_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()