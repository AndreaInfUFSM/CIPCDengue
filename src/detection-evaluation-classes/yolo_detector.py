from detector_interface import DetectorInterface
from ultralytics import YOLO

class YoloObjectDetector(DetectorInterface):

        

    def __init__(self, path):
        super().__init__(path)
        self.model_fn = self.get_model_fn(path)


    def get_model_fn(self, model_path):
        
        #model_pt = '/home/andrea/Dropbox/lsc/dengue/training-round-02/yolo-trained-model/v5-best.pt'

        model_fn = YOLO(model_path)  # load the trained model
        return model_fn
    



         
    # Denormalize predicted bboxes' elements
    def denormalize_fn(self, element):
        return int(element / 256 * 416)    

    def get_predictions_for_image(self, image):        


        result = self.model_fn(image) # .jpg
        # print(result[0].boxes)

        bboxes = [[int(n) for n in box] for box in result[0].boxes.xyxy.tolist()]
        # print(bboxes)

        labels = [int(label) for label in result[0].boxes.cls.tolist()]
        scores = result[0].boxes.conf.tolist()
        # print(scores)

    
            
        return bboxes, labels, scores


    def get_predictions_for_dataset(self, ds):
        # Initialize lists to store predictions 
        fnames = []
        bboxes = []
        labels = []
        scores = []
        
        for entry in ds.get_data():
            
            img_name = entry['fname'] #fname.numpy().decode('utf-8')
        
            print(f'Detector applied to image {img_name}')
            pred_bboxes, pred_labels, pred_scores = self.get_predictions_for_image(entry['image'])
            fnames.append(img_name)
            bboxes.append(pred_bboxes)
            labels.append(pred_labels)
            scores.append(pred_scores)

            
            
        return fnames, bboxes, labels, scores