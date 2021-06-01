import os
import sys
from argparse import ArgumentParser, SUPPRESS
from math import exp as exp
from time import time
from PIL import Image
import numpy as np
import cv2
from openvino.inference_engine import IENetwork, IECore
import logging

logging.basicConfig(format="[ %(levelname)s ] %(message)s", level=logging.INFO, stream=sys.stdout)
log = logging.getLogger()

def main():
    log.info("Creating Inference Engine...")
    ie = IECore()
    model_xml = 'keras_model/angle_with_light_linear.xml'
    model_bin = 'keras_model/angle_with_light_linear.bin'
    # 加载模型
    log.info("Loading network files:\n\t{}\n\t{}".format(model_xml, model_bin))
    net1 = IENetwork(model=model_xml, weights=model_bin)
    # 准备输入
    log.info("Preparing inputs")
    input_blob = next(iter(net1.inputs))
    net1.batch_size = 1

    # 装载模型
    log.info("Loading model to the plugin")
    exec_net1 = ie.load_network(network=net1, num_requests=2, device_name='MYRIAD')  # num_requests注意
    image = Image.open("4.jpg")  # 用PIL中的Image.open打开图像
    img_arr = np.array(image)  # 转化成numpy数组
    img_arr = img_arr.reshape((1,) + img_arr.shape)  # 160,120,3变成1,160,120,3
    # 推理
    exec_net1.start_async(request_id=0, inputs={input_blob: img_arr})
    # 获取输出
    if exec_net1.requests[0].wait(-1) == 0:
        output = exec_net1.requests[0].outputs
        throttle_binned = output['throttle_out/Softmax']
        angle_binned = output['angle_out/Softmax']
        N = len(throttle_binned[0])
        throttle = linear_unbin(throttle_binned, N=N,
                                offset=0.0, R=0.5)
        angle = linear_unbin(angle_binned)
        print(angle, throttle)

def linear_unbin(arr, N=15, offset=-1, R=2.0):
    '''
    preform inverse linear_bin, taking
    one hot encoded arr, and get max value
    rescale given R range and offset
    '''
    b = np.argmax(arr)
    a = b * (R / (N + offset)) + offset
    return a

if __name__ == '__main__':
    main()