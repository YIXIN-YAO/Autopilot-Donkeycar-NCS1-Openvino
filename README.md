# README
21年5月份做的一个项目。  
搭载树莓派4B的小车通过深度学习实现自动巡线、识别红路灯加速减速。树莓派外接Intel神经计算棒实现加速推理。  
执行mycar文件夹中的drive函数启动小车：  
`python manage.py drive --model models/angle_with_light13.xml`  
其它代码在donkeycar文件夹里，上传到了release。  
release里有很多其它文件，是我之前通过github把一些训练需要的文件上传到kaggle用的。

使用的是微雪的车模  
donkeycar版本：3.1  
openvino版本2019.3 因为计算棒是NCS一代，所以openvino也用的比较老的版本。

项目是在开源项目donkeycar上做了修改,官方仓库地址：https://github.com/autorope/donkeycar
巡线和识别红绿灯用了两个模型，并且使用了计算棒加速，所以修改了donkeycar\donkeycar\parts文件夹下的keras.py,修改了模型训练，推理相关的代码。
然后还对遥控器的功能做了些简单修改。

演示视频：

![demo](3.gif)
