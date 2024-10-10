import time
import drag

from OCR import OCR

WAIT_FOR_START_X = 555
WAIT_FOR_START_Y = 125
WAIT_FOR_WIDTH = 100
WAIT_FOR_HEIGHT = 25

NUM1_START_X = 280
NUM1_START_Y = 500
NUM1_WIDTH = 200
NUM1_HEIGHT = 100

NUM2_START_X = 620
NUM2_START_Y = 500
NUM2_WIDTH = 200
NUM2_HEIGHT = 100

begin = False

while (True):
    
    while (not begin):
        print("正在等待开始...")
        # 判断是否进入界面
        if (OCR(WAIT_FOR_START_X, WAIT_FOR_START_Y, WAIT_FOR_WIDTH, WAIT_FOR_HEIGHT) == '10题' or OCR(WAIT_FOR_START_X, WAIT_FOR_START_Y, WAIT_FOR_WIDTH, WAIT_FOR_HEIGHT) == '(10题'):
            begin = True
    
    temp_num1 = OCR(NUM1_START_X, NUM1_START_Y, NUM1_WIDTH, NUM1_HEIGHT)
    temp_num2 = OCR(NUM2_START_X, NUM2_START_Y, NUM2_WIDTH, NUM2_HEIGHT)
    while (not temp_num1.isdigit() or temp_num1[0] == '0'):
        temp_num1 = OCR(NUM1_START_X, NUM1_START_Y, NUM1_WIDTH, NUM1_HEIGHT)
    while (not temp_num2.isdigit() or temp_num2[0] == '0'):
        temp_num2 = OCR(NUM2_START_X, NUM2_START_Y, NUM2_WIDTH, NUM2_HEIGHT)
    if (temp_num1 == '' and temp_num2 == ''):
        break
    print(f"num1={temp_num1}, num2={temp_num2}")
    if (int(temp_num1) > int(temp_num2)):
        print("大于")
        drag.print_larger_than()
    else:
        print("小于")
        drag.print_less_than()
    time.sleep(0.25)