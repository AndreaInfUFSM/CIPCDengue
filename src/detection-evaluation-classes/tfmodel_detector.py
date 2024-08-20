from detector_interface import DetectorInterface

import logging
logging.getLogger('tensorflow').setLevel(logging.ERROR)

import os
# Set the environment variable before TensorFlow is imported
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf

class TFObjectDetector(DetectorInterface):

        

    def __init__(self, path):
        super().__init__(path)
        self.model_fn = self.get_model_fn(path)


    def get_model_fn(self, saved_model_path):
        
      #saved_model_path = '/home/andrea/Dropbox/lsc/dengue/tensorflow-conda/aedes-egg-detection-3000steps/exported_model/'
      # Load the saved model
      # model = tf.keras.models.load_model(saved_model_path)
      # model = keras.layers.TFSMLayer(saved_model_path, call_endpoint='serving_default')

      imported = tf.saved_model.load(saved_model_path)
      model_fn = imported.signatures['serving_default'] 
      return model_fn
    



         
    # Denormalize predicted bboxes' elements
    def denormalize_fn(self, element):
        return int(element / 256 * 416)    

    def get_predictions_for_image(self, image):        

        input_tensor = tf.convert_to_tensor(image)
        input_tensor = input_tensor[tf.newaxis, ...]  # Add batch dimension

        detections = self.model_fn(input_tensor) # This may take long       
        
        # All these lists will have the same size (100)
        # WARNING: This will not going to work if we expect to have more than 100 objects in the image
        # TODO: Where does this size (100) come from? How to know when we need to check more than 100 objects? 
        bboxes = [[self.denormalize_fn(element) for element in box] for box in detections['detection_boxes'][0].numpy().tolist()]
        bboxes = [[box[1],box[0],box[3],box[2]] for box in bboxes] #xyxy instead of yxyx
        labels = detections['detection_classes'][0].numpy().tolist()
        #scores = detections['detection_scores'][0]
        scores = detections['detection_scores'][0].numpy().tolist()
        
    
            
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


