class PredictionEvaluator:

    
    @staticmethod
    def match_predictions_to_groundtruth(pred_bboxes, truth_bboxes, iou_threshold):

        true_positive_count = 0
        false_positive_count = 0
        false_negative_count = 0
        
        matched_count = 0
        matched_indices = set()
        
        # For each prediction
        for i, pred_box in enumerate(pred_bboxes):
            best_iou = 0
            best_match = -1
            # Find the best match for this prediction among truth_boxes
            for j, truth_box in enumerate(truth_bboxes):
                iou = PredictionEvaluator.calculate_iou(pred_box, truth_box)
                if iou > best_iou:
                    best_iou = iou
                    best_match = j
            
            if best_iou >= iou_threshold and best_match not in matched_indices:
                matched_indices.add(best_match)
     
                true_positive_count += 1
            else:
      
                false_positive_count += 1
        
        for j in range(len(truth_bboxes)):
            if j not in matched_indices:
                false_negative_count += 1

        matched_count = len(matched_indices)
        
        result = {
            'pred_count': len(pred_bboxes),
            'matched_count': matched_count,
            'true_positive_count': true_positive_count,
            'false_positive_count': false_positive_count,
            'false_negative_count': false_negative_count
        }
        return result


    
    
    # Cada imagem corresponde a um conjunto de bboxes e a um conjunto de preds
    @staticmethod
    def evaluate(truth_bboxes, pred_bboxes, iou_threshold):

        vars = {
            'pred_sum': 0,
            'matched_sum': 0,
            'true_positive_sum': 0,
            'false_positive_sum': 0,
            'false_negative_sum': 0,
        }

        print('Len of truth_boxes', len(truth_bboxes))
        # For each image
        for i in range(0, len(truth_bboxes)):

            eval = PredictionEvaluator.match_predictions_to_groundtruth(pred_bboxes[i], truth_bboxes[i], iou_threshold)

            vars['pred_sum'] += eval['pred_count']
            vars['matched_sum'] += eval['matched_count']
            vars['true_positive_sum'] += eval['true_positive_count']
            vars['false_positive_sum'] += eval['false_positive_count']
            vars['false_negative_sum'] += eval['false_negative_count']

        vars['precision'] = vars['true_positive_sum'] / (vars['true_positive_sum'] + vars['false_positive_sum'])
        vars['recall'] = vars['true_positive_sum'] / (vars['true_positive_sum'] + vars['false_negative_sum'])
        vars['f1score'] = 2 * (vars['precision'] * vars['recall']) / (vars['precision'] + vars['recall'])
            
        return vars

    @staticmethod
    def calculate_iou(box1, box2):
        """
        Calculates the Intersection-over-Union (IoU) between two bounding boxes.
        
        Args:
            bbox1 (list): The first bounding box [x1, y1, x2, y2].
            bbox2 (list): The second bounding box [x1, y1, x2, y2].
        
        Returns:
            float: The IoU value.
        """
        # Compute intersection
        x1 = max(box1[0], box2[0])
        y1 = max(box1[1], box2[1])
        x2 = min(box1[2], box2[2])
        y2 = min(box1[3], box2[3])
        intersection = max(0, x2 - x1) * max(0, y2 - y1)
        
        # Compute union
        box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
        box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
        union = box1_area + box2_area - intersection
        
        return intersection / union      