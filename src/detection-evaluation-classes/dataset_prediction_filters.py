

def filter_equal(value, source_list, target_lists):
    mask = [element == value for element in source_list]
    output_lists = [[element for element, mask in zip(source_list, mask) if mask]]
    for each_list in target_lists:
        output_lists.append([element for element, mask in zip(each_list, mask) if mask])
    return output_lists
    

def filter_greater(value, source_list, target_lists):
    mask = [element > value for element in source_list]
    output_lists = [[element for element, mask in zip(source_list, mask) if mask]]
    for each_list in target_lists:
        output_lists.append([element for element, mask in zip(each_list, mask) if mask])
    return output_lists




# @staticmethod
# def filter_image_predictions_by_score(score_threshold, predicted_bboxes, predicted_labels, predicted_scores):

#     score_mask = [score > score_threshold for score in predicted_scores]

#     filtered_bboxes = [bbox for bbox, mask in zip(predicted_bboxes, score_mask) if mask]
#     filtered_labels = [label for label, mask in zip(predicted_labels, score_mask) if mask]
#     filtered_scores = [score for score, mask in zip(predicted_scores, score_mask) if mask]

#     return filtered_bboxes, filtered_labels, filtered_scores

# @staticmethod
# def filter_image_predictions_by_class(class_id, predicted_bboxes, predicted_labels, predicted_scores):

#     class_mask = [label == class_id for label in predicted_labels]

#     filtered_bboxes = [bbox for bbox, mask in zip(predicted_bboxes, class_mask) if mask]
#     filtered_labels = [label for label, mask in zip(predicted_labels, class_mask) if mask]
#     filtered_scores = [score for score, mask in zip(predicted_scores, class_mask) if mask]

#     return filtered_bboxes, filtered_labels, filtered_scores

def filter_image_groundtruth(class_id, bboxes, labels):
    class_mask = [label == class_id for label in labels]
    filtered_labels = [label for label, mask in zip(labels, class_mask) if mask]
    filtered_bboxes = [bbox for bbox, mask in zip(bboxes, class_mask) if mask]
        
    return filtered_bboxes, filtered_labels

    
def filter_dataset_groundtruth(class_id, ds_bboxes, ds_labels):

    assert len(ds_bboxes) == len(ds_labels), "Lenghts of dataset bboxes and labels should be equal"

    filtered_ds_bboxes = []
    filtered_ds_labels = []

    number_of_images = len(ds_bboxes)

    for i in range(0, number_of_images):
        filtered_bboxes, filtered_labels = filter_image_groundtruth(class_id, ds_bboxes[i], ds_labels[i])
        filtered_ds_bboxes.append(filtered_bboxes)
        filtered_ds_labels.append(filtered_labels)
        
        # class_mask = [label == class_id for label in ds_labels[i]]
        # filtered_ds_labels.append([label for label, mask in zip(ds_labels[i], class_mask) if mask])
        # filtered_ds_bboxes.append([bbox for bbox, mask in zip(ds_bboxes[i], class_mask) if mask])
        
    return filtered_ds_bboxes, filtered_ds_labels




def filter_image_predictions_by_score(score_threshold, predicted_bboxes, predicted_labels, predicted_scores):


    score_mask = [score > score_threshold for score in predicted_scores]
    filtered_bboxes = [bbox for bbox, mask in zip(predicted_bboxes, score_mask) if mask]
    filtered_labels = [label for label, mask in zip(predicted_labels, score_mask) if mask]
    filtered_scores = [label for label, mask in zip(predicted_scores, score_mask) if mask]


    # class_mask = [label == class_id for label in predicted_labels]

    # filtered_bboxes = [bbox for bbox, mask in zip(predicted_bboxes, class_mask) if mask]
    # filtered_labels = [label for label, mask in zip(predicted_labels, class_mask) if mask]
    # filtered_scores = [score for score, mask in zip(predicted_scores, class_mask) if mask]

    return filtered_bboxes, filtered_labels, filtered_scores


def filter_image_predictions_by_class_and_score(class_id, score_threshold, predicted_bboxes, predicted_labels, predicted_scores):


    score_mask = [score > score_threshold for score in predicted_scores]
    filtered_bboxes = [bbox for bbox, mask in zip(predicted_bboxes, score_mask) if mask]
    filtered_labels = [label for label, mask in zip(predicted_labels, score_mask) if mask]
    filtered_scores = [label for label, mask in zip(predicted_scores, score_mask) if mask]

    class_mask = [label == class_id for label in predicted_labels]
    filtered_pred_bboxes = [bbox for bbox, mask in zip(filtered_bboxes, class_mask) if mask]
    filtered_pred_labels = [label for label, mask in zip(filtered_labels, class_mask) if mask]
    filtered_pred_scores = [label for label, mask in zip(filtered_scores, class_mask) if mask]


    # class_mask = [label == class_id for label in predicted_labels]

    # filtered_bboxes = [bbox for bbox, mask in zip(predicted_bboxes, class_mask) if mask]
    # filtered_labels = [label for label, mask in zip(predicted_labels, class_mask) if mask]
    # filtered_scores = [score for score, mask in zip(predicted_scores, class_mask) if mask]

    return filtered_pred_bboxes, filtered_pred_labels, filtered_pred_scores

def filter_dataset_predictions(class_id, score_threshold, predicted_bboxes, predicted_labels, predicted_scores):
    
    assert len(predicted_bboxes) == len(predicted_labels) and len(predicted_labels) == len(predicted_scores), "Lenghts of bboxes, labels and scores should be equal"

    filtered_pred_labels = []
    filtered_pred_bboxes = []
    
    number_of_images = len(predicted_bboxes)

    for i in range(0, number_of_images):

        filtered_bboxes, filtered_labels, _ = filter_image_predictions_by_class_and_score(class_id, score_threshold, predicted_bboxes[i], predicted_labels[i], predicted_scores[i])
        filtered_pred_labels.append(filtered_labels)
        filtered_pred_bboxes.append(filtered_bboxes)
    

        # score_mask = [score > score_threshold for score in predicted_scores[i]]
        # filtered_bboxes = [bbox for bbox, mask in zip(predicted_bboxes[i], score_mask) if mask]
        # filtered_labels = [label for label, mask in zip(predicted_labels[i], score_mask) if mask]

        # class_mask = [label == class_id for label in predicted_labels[i]]
        # filtered_pred_bboxes.append([bbox for bbox, mask in zip(filtered_bboxes, class_mask) if mask])
        # filtered_pred_labels.append([label for label, mask in zip(filtered_labels, class_mask) if mask])

        
    return filtered_pred_bboxes, filtered_pred_labels