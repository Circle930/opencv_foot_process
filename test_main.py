import cv2
import numpy as np
from matplotlib import pyplot as plt
from crop_plastic_board import crop_plastic_board
from detect_foot_direction import detect_foot_direction
from split_image_vertically import split_image_vertically
from process_image import process_image
from calculate_black_white_ratio import calculate_black_white_ratio


def process_and_analyze_foot(cropped_img, side):
    try:
        if cropped_img is not None:
            # 计算黑白像素的比例
            black_ratio, white_ratio = calculate_black_white_ratio(cropped_img)

            # 输出白色像素占比
            # print(f"{side}脚 - 白色像素占比: {white_ratio:.2%}")

            # 判断足型并输出相应信息
            if 0.35 < white_ratio < 0.75:
                print(f"{side}脚 - 足型：正常")
                print("建议：选择舒适合脚的鞋类，适度进行足弓锻炼，定期检查足部健康。")
            elif white_ratio <= 0.35:
                print(f"{side}脚 - 足型：高弓足")
                print("建议：选择具有足弓缓震设计的鞋款，进行足部柔软度和伸展锻炼。")
            else:
                print(f"{side}脚 - 足型：扁平足")
                print("建议：选择具有良好足弓支撑的鞋款，使用定制或适用于扁平足的矫形鞋垫，进行足弓锻炼。")
        else:
            print(f"{side}脚 - 无法读取图片，请检查路径是否正确。")
    except ZeroDivisionError:
        print(f"{side}脚 - 图片中没有白色像素，无法计算比例。")
    except Exception as e:
        print(f"{side}脚 - 发生异常: {str(e)}")


# 导入处理图片路径
img_path = 'sample_images/foot.jpg'

# 调用函数裁剪塑料板部分  
result_image = crop_plastic_board(img_path)

# 调用函数识别塑料板（脚印）方向
direction, result_img, edges = detect_foot_direction(result_image)

# 调用函数纵向切割为左右脚
left_half, right_half = split_image_vertically(result_img)

# 调用函数对左右脚进行轮廓处理
process_image_L, cropped_img_L = process_image(left_half)
process_image_R, cropped_img_R = process_image(right_half)

# 调用函数判断左右脚的足型
process_and_analyze_foot(cropped_img_L, "您的左")
process_and_analyze_foot(cropped_img_R, "您的右")



#----------------------------------------------------------------



# 显示原始图片和截取的图片
cv2.imshow('Original Image', cv2.imread(img_path))
cv2.imshow('Cropped Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 显示处理后的图像和边缘
if isinstance(result_img, np.ndarray):
    plt.subplot(121), plt.imshow(result_img, cmap='gray')
    plt.title('Result Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Canny Edges'), plt.xticks([]), plt.yticks([])

    plt.show()

print("脚掌位置:", direction)

# 显示从中线分割
if left_half is not None and right_half is not None:
    # 显示分割后的左右两半图片
    cv2.imshow('Left Half', left_half)
    cv2.waitKey(0)
    cv2.imshow('Right Half', right_half)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 显示绘制的轮廓图像
cv2.imshow('Contour Image', process_image_L)
cv2.waitKey(0)
cv2.imshow('Contour Image', process_image_R)
cv2.waitKey(0)
cv2.imshow('L',cropped_img_L)
cv2.waitKey(0)
cv2.imshow('R',cropped_img_R)
cv2.waitKey(0)
cv2.destroyAllWindows
