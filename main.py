#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import tensorflow as tf


from utils import tester

def main():
    ts = tester.Tester(5)
    ts.testAll(3, 1)
    ts.testTensorFlowRandom(stepSize=0.01, hiddenLayers=2, layerNodes=2, activation_function=tf.tanh)
    ts.testTensorFlow(stepSize=0.01, hiddenLayers=2, layerNodes=2, activation_function=tf.tanh)


if __name__ == '__main__':
    main()