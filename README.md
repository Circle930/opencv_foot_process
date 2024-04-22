# 基于OpenCv的足底🦶分割

## 安装环境
运行foot_process目录下的requirements.txt
```
pip install -r requirements.txt
```

## 图像预处理步骤⬇每个文件的功能⬇️👀
- process_image：
  - 获取图像的宽度和高度，直接使用图像的第二个通道二值化
  - 高斯模糊处理、腐蚀、膨胀、自动阈值二值化
  - 确定图像的有效范围`valid_area = (0, 0, width, height)`、创建一个与原图大小相同的黑色图像，用于绘制轮廓、只保留下脚弓部分
- detect_foot_direction：
  - 判断是否为长条型镂空区域，可根据实际情况调整阈值
  - 目的是摆正板子
- crop_plastic_board：裁剪板子与删除背景
- split_image_verticaly：裁剪图像为左脚和右脚
- calculate_black_white_ratio：计算足弓与足底占比
- main：调用以上函数⬆️
  - ```
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
    ```
### 提示🔔：test文件是用来调试测试用的，可以不用管它