import cv2

def split_image_vertically(img):

    if img is None:
        print("无法读取图片，请检查路径是否正确。")
        return None, None

    # 获取图片的高度和宽度
    height, width = img.shape[:2]

    # 计算需要裁剪的高度
    crop_top = int(height / 5)
    crop_bottom = int(height / 7)

    # 计算需要裁剪的宽度
    crop_left = int(width / 7)

    # 裁剪图像
    img_cropped = img[crop_top:-crop_bottom, crop_left:]

    # 计算中间位置的列索引
    middle = img_cropped.shape[1] // 2

    # 分割裁剪后的图片为左右两半
    left_half = img_cropped[:, :middle]
    right_half = img_cropped[:, middle:]

    return left_half, right_half

# # 示例用法
# image_path = 'sample_images/LL.jpg'
# left_half, right_half = split_image_vertically(image_path)

# if left_half is not None and right_half is not None:
#     # 显示分割后的左右两半图片
#     cv2.imshow('Left Half', left_half)
#     cv2.waitKey(0)
#     cv2.imshow('Right Half', right_half)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
