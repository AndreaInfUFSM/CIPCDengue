import os
# Set the environment variable before TensorFlow is imported
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
tf.get_logger().setLevel('ERROR')

import absl.logging
absl.logging.set_verbosity(absl.logging.ERROR)

from tf_dataset import TFDataset
from tfmodel_detector import TFObjectDetector
from yolo_dataset import YoloDataset
from yolo_detector import YoloObjectDetector
from boundingbox_visualizer import BoundingBoxVisualizer
from prediction_evaluator import PredictionEvaluator
from dataset_prediction_filters import *



def test_inspect_single_prediction(entry_name, str_framework, dataset_class, detector_class, dataset_path, model_path):

    print(f'\nEvaluating predictions for a single image using {str_framework}. This may take a little long to initialize...')

    dataset = dataset_class(dataset_path)
    detector = detector_class(model_path)
    image, _, _ = dataset.get_entry_by_fname(entry_name)
    predicted_bboxes, predicted_labels, predicted_scores = detector.get_predictions_for_image(image)
    
    print('\nPrediction output, without filtering')
    print('\nPredicted boxes:', len(predicted_bboxes))
    print(predicted_bboxes)
    print('\nPredicted labels:', len(predicted_labels))
    print(predicted_labels)
    print('\nPredicted scores:', len(predicted_scores))
    print(predicted_scores)





def test_evaluate_prediction(str_framework, dataset_class, detector_class, dataset_path, model_path, score_threshold, iou_threshold):

    print(f'\nEvaluating predictions for a whole dataset using {str_framework}. This may take long...')

    dataset = dataset_class(dataset_path)
    detector = detector_class(model_path)

    fnames, groundtruth_bboxes, groundtruth_labels = dataset.get_groundtruths()
    fnames, predicted_bboxes, predicted_labels, predicted_scores = detector.get_predictions_for_dataset(dataset)

    for class_id in dataset.get_unique_classes():

        print(f'\n\nMetrics for class {class_id} using {str_framework}:')
        filtered_truth_bboxes, filtered_truth_labels = filter_dataset_groundtruth(class_id, groundtruth_bboxes, groundtruth_labels)
        filtered_pred_bboxes, filtered_pred_labels = filter_dataset_predictions(class_id, score_threshold, predicted_bboxes, predicted_labels, predicted_scores)
        
        # print(filtered_truth_bboxes)
        # print(filtered_truth_labels)
        # print(filtered_pred_bboxes)

        confusion_matrix_for_class = PredictionEvaluator.evaluate(filtered_truth_bboxes, filtered_pred_bboxes, iou_threshold)
        print(confusion_matrix_for_class)    



def main():

    score_threshold = 0.75
    iou_threshold = 0.45

    tf_test_dataset_path = '/home/andrea/Dropbox/lsc/dengue/training-round-02/round-02-tiled-training-dataset/v5-test.tfrecord'
    tf_saved_model_path = '/home/andrea/Dropbox/lsc/dengue/training-round-02/tf-trained-model/kaggle/working/exported_model/'
    # test_inspect_single_prediction('0', 'Tensorflow', TFDataset, TFObjectDetector, tf_test_dataset_path, tf_saved_model_path)
    test_evaluate_prediction('Tensorflow', TFDataset, TFObjectDetector, tf_test_dataset_path, tf_saved_model_path, score_threshold, iou_threshold)
    

    yolo_test_dataset_path = '/home/andrea/Dropbox/lsc/dengue/training-round-02/root-dir-to-upload/images/test/'
    yolo_model_pt = '/home/andrea/Dropbox/lsc/dengue/training-round-02/yolo-trained-model/v5-best.pt'
    # test_inspect_single_prediction('000000000379.jpg', 'Yolo', YoloDataset, YoloObjectDetector, yolo_test_dataset_path, yolo_model_pt)
    # test_evaluate_prediction('Yolo', YoloDataset, YoloObjectDetector, yolo_test_dataset_path, yolo_model_pt, score_threshold, iou_threshold)

if __name__ == "__main__":
    main()