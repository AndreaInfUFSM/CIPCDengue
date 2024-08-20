from prediction_evaluator import PredictionEvaluator
from dataset_prediction_filters import *

score_threshold = 0.75
iou_threshold = 0.45

def test_calculate_iou():
    
    print("\n==> Testing calculate_iou():")

    iou_value = PredictionEvaluator.calculate_iou([50, 50, 100, 100], [55, 55, 95, 95])
    print(f"IoU value: {iou_value}")
    iou_value = PredictionEvaluator.calculate_iou([55, 55, 95, 95], [50, 50, 100, 100])
    print(f"IoU value: {iou_value}")
    iou_value = PredictionEvaluator.calculate_iou([140, 140, 190, 190], [150, 150, 200, 200])
    print(f"IoU value: {iou_value}")
    iou_value = PredictionEvaluator.calculate_iou([140, 140, 195, 195], [150, 150, 200, 200])
    print(f"IoU value: {iou_value}")


def test_evaluate():

    print("\n==> Testing evaluate():")

    # Example ground truth and predicted data, only one class
    groundtruth_bboxes = [[[50, 50, 100, 100], [150, 150, 200, 200]]]
    groundtruth_labels = [[1, 1]]

    predicted_bboxes = [[[55, 55, 95, 95], [140, 140, 195, 195]]]
    predicted_labels = [[1, 1]]
    predicted_scores = [[score_threshold + 0.01, 0.65]]
    #predicted_scores = [[score_threshold, 0.65]] # ZeroDivisionError: division by zero

    
    print("\nNo filtering")
    result = PredictionEvaluator.evaluate(groundtruth_bboxes, predicted_bboxes, iou_threshold)
    print(result)


    print("\nAfter filtering")
    # Filter classes and scores before evaluating
    class_id = 1
    filtered_truth_bboxes, filtered_truth_labels = filter_dataset_groundtruth(class_id, groundtruth_bboxes, groundtruth_labels)
    print(filtered_truth_bboxes)
    filtered_pred_bboxes, filtered_pred_labels = filter_dataset_predictions(class_id, score_threshold, predicted_bboxes, predicted_labels, predicted_scores)
    print(filtered_pred_bboxes)

    result = PredictionEvaluator.evaluate(filtered_truth_bboxes, filtered_pred_bboxes, iou_threshold)
    print(result)



def main():

    test_calculate_iou()
    test_evaluate()




if __name__ == "__main__":
    main()