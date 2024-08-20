from dataset_interface import DatasetInterface

import os
# Set the environment variable before TensorFlow is imported
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
#import numpy as np


class TFDataset(DatasetInterface):
        

    def __init__(self, path):
        super().__init__(path)
        self.data = self.parse_from_path(path)
                  
        
    def parse_tfrecord_fn(self, example):
        feature_description = {
            'image/height': tf.io.FixedLenFeature((), tf.int64),
            'image/width': tf.io.FixedLenFeature((), tf.int64),
            'image/encoded': tf.io.FixedLenFeature([], tf.string),
            'image/filename': tf.io.FixedLenFeature([], tf.string),
            'image/object/class/label': tf.io.VarLenFeature(tf.int64),
            'image/object/bbox/xmin': tf.io.VarLenFeature(tf.float32),
            'image/object/bbox/xmax': tf.io.VarLenFeature(tf.float32),
            'image/object/bbox/ymin': tf.io.VarLenFeature(tf.float32),
            'image/object/bbox/ymax': tf.io.VarLenFeature(tf.float32),
        }

        example = tf.io.parse_single_example(example, feature_description)
        
        fname = example['image/filename'] 
        width = example['image/width']
        height = example['image/height']

        image = tf.image.decode_jpeg(example['image/encoded'])
        labels = tf.sparse.to_dense(example['image/object/class/label'])
        xmin = tf.sparse.to_dense(example['image/object/bbox/xmin'])
        xmax = tf.sparse.to_dense(example['image/object/bbox/xmax'])
        ymin = tf.sparse.to_dense(example['image/object/bbox/ymin'])
        ymax = tf.sparse.to_dense(example['image/object/bbox/ymax'])

        #bboxes = tf.stack([xmin, ymin, xmax, ymax], axis=1)
        bboxes = tf.stack([ymin, xmin, ymax, xmax], axis=1)

        return fname, image, width, height, labels, bboxes

    # Recebe dataset e itera sobre ele, construindo um array de dict
    def parse_from_path(self, ds_path):

        ds = tf.data.TFRecordDataset(ds_path)
        ds = ds.map(self.parse_tfrecord_fn)
        ds = ds.as_numpy_iterator()
        arr = []
        for fname, image, width, height, labels, bboxes in ds:
            dict = {}
            dict['image'] = image 
            dict['fname'] = fname.decode('utf-8')
            dict['norm_yxyx'] = bboxes 
            dict['yxyx'] = [[int(box[0]*height), int(box[1]*width), int(box[2]*height), int(box[3]*width)] for box in bboxes]
            dict['bboxes'] = [[box[1], box[0], box[3], box[2]] for box in dict['yxyx']]
            dict['labels'] = labels.tolist()
            arr.append(dict)

        return arr


