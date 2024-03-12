import cv2
import numpy as np

def process_image(img):

    if img is None:
        print("无法读取图片，请检查路径是否正确。")
        return None

    # 获取图像的宽度和高度
    height, width = img.shape[:2]

    # 直接使用图像的第二个通道
    img_channel = img[:, :, 1]

    # 高斯模糊处理
    img_blur = cv2.GaussianBlur(img_channel, (11, 11), sigmaX=0, sigmaY=0)

    # 腐蚀
    kernel = np.ones((20, 20), np.uint8)
    img_erode = cv2.erode(img_blur, kernel, iterations=1)

    # 膨胀
    img_dilate = cv2.dilate(img_erode, kernel, iterations=1)

    # 自动阈值二值化
    ret, thresh = cv2.threshold(img_dilate, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 确定图像的有效范围
    valid_area = (0, 0, width, height)

    # 创建一个与原图大小相同的黑色图像，用于绘制轮廓
    contour_img = np.zeros_like(img)

    cropped_img = None

    for cnt in contours:
        # 近似轮廓
        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        # 获取轮廓的边界框
        x, y, w, h = cv2.boundingRect(approx)
        bounding_box = (x, y, x + w, y + h)

        # 获取近似后的轮廓的顶点数量
        num_vertices = len(approx)

        # 添加条件：如果轮廓不是直线
        if num_vertices > 3:  # 这里假设至少有3个顶点，你可以根据实际情况调整阈值
            # 检查边界框是否与图像的有效范围相交
            if all(
                (box[0] < valid_area[2] and box[2] > valid_area[0] and box[1] < valid_area[3] and box[3] > valid_area[1])
                for box in [bounding_box, valid_area]
            ):
                # 在图像上绘制轮廓
                cv2.drawContours(contour_img, [cnt], -1, (255, 255, 255), thickness=cv2.FILLED)

                hull = cv2.convexHull(cnt)
                cv2.polylines(contour_img, [hull], isClosed=True, color=(255, 255, 255), thickness=2)

                # 裁剪图像
                cropped_img = contour_img[y:y + h, x:x + w]

                # 计算裁剪后图像的面积
                cropped_area = w * h

                # 判断面积
                if cropped_area < 30000:
                    continue

    # 只保留下脚弓部分
    crop_top = int(height * 1.5 / 5)
    crop_bottom = int(height / 5)
    cropped_img = cropped_img[crop_top:-crop_bottom, :]

    return contour_img, cropped_img

# # 示例用法
# image_path = 'sample_images/RR.jpg'
# contour_img, process = process_image(image_path)

# # 显示绘制的轮廓图像
# cv2.imshow('Contour Image', contour_img)
# cv2.waitKey(0)

# # 显示裁剪后的图像
# cv2.imshow('Cropped Image', process)
# cv2.waitKey(0)

# cv2.destroyAllWindows()