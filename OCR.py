import pyautogui
import easyocr
import cv2
import numpy as np

# 创建 EasyOCR 读取器，指定语言
reader = easyocr.Reader(['ch_sim'])  # 可以根据需要添加其他语言，例如 ['ch_sim'] 代表简体中文

def OCR(x, y, width, height):
    # 获取屏幕截图
    screenshot = pyautogui.screenshot()

    # 将截图转换为 NumPy 数组
    screenshot_np = np.array(screenshot)

    # 转换颜色空间，从 RGB 转为 BGR
    screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # 提取 ROI
    roi = screenshot_bgr[y:y+height, x:x+width]

    # 使用 EasyOCR 进行 OCR 识别
    result = reader.readtext(roi)

    # 提取识别的文本
    text = ' '.join([item[1] for item in result])  # item[1] 是识别的文本
    # print(f"x={x}, y={y}, width={width}, height={height}, 识别结果为={text}")

    # 可选：显示 ROI 图像
    # cv2.imshow("ROI", roi)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows() 

    return text