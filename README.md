# 基于 OCR 的小猿口算 PK 比大小脚本

---

注意，此方法是直接对本地的 Android 模拟器进行截图识别和模拟鼠标操作的，一秒一题，速度较慢，且没有做任何性能上和使用便捷度上的优化，仅图一乐，若追求更快的写题速度或更好的使用体验，请移步寻找其他方法。

## Feature

- 使用 EasyOCR 对指定的 ROI 进行截取识别
- 模拟鼠标拖拽手势输入回答

## Installation

1. Clone the repository:
```shell
git clone https://github.com/Sen-Yao/Xiaoyuan_PK.git
cd Xiaoyuan_PK 
```

2. Set up a virtual environment (optional but recommended):

```shell
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Usage

在 Windows 上，首先打开任意一个安卓模拟器，并安装小猿口算 APP。

由于本代码没有做模拟器窗口的定位（问就是懒），因此请确保**每次将模拟器窗口放置在同一位置**，然后根据自己的窗口位置填写以下常量，如果代码不能正常运行，多半是因为下面的常量没有配置好。这个方法很蠢，如果您有更好的方法，欢迎提 pr。

1. 小猿口算窗口的输入区域

在 drag.py 下

- DRAGGING_SCREEN_START_X
- DRAGGING_SCREEN_START_Y
- DRAGGING_SCREEN_END_X
- DRAGGING_SCREEN_END_Y

2. 用于检测是否开始的“X/10题”

为了判断比赛是否开始，这里需要告诉程序当 PK 比赛开始时出现的 “X/10题” 的字样在哪里出现。

在 main.py 下

- WAIT_FOR_START_X
- WAIT_FOR_START_Y
- WAIT_FOR_WIDTH
- WAIT_FOR_HEIGHT

3. 两个数字的位置

在 main.py 下

- NUM1_START_X
- NUM1_START_Y
- NUM1_WIDTH
- NUM1_HEIGHT

- NUM2_START_X
- NUM2_START_Y
- NUM2_WIDTH
- NUM2_HEIGHT

确保以上代码修改正确后直接运行

```shell
python main.py
```



## License

This project is licensed under the MIT License. See the LICENSE file for details.
