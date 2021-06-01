# mydonkeycar
21年5月份做的一个项目。
搭载树莓派4B的小车通过深度学习实现自动巡线、识别红路灯加速减速。树莓派外接Intel神经计算棒实现加速推理。
执行mycar文件夹中的drive函数启动小车，其它代码在release的donkeycar文件夹里。release里有很多其它的文件，是我之前通过github把一些训练需要的文件上传到kaggle用的。

项目是在开源项目donkeycar上做了修改，巡线和识别红绿灯用了两个模型，并且使用了计算棒加速，所以修改了donkeycar\donkeycar\parts文件夹下的keras.py,修改了模型训练，推理相关的代码。
然后还对遥控器的功能做了些简单修改。
![demo](3.gif)
