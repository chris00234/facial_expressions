import numpy as np
import pandas as pd
import cv2 as cv
import PIL.Image as Image
import tensorflow as tf
from tensorflow import keras


def read_csv(path):
    df = pd.read_csv(path)
    return df

df1 = read_csv('/Users/chrischo/Documents/cs178/facial_expressions/data/500_picts_satz.csv')

