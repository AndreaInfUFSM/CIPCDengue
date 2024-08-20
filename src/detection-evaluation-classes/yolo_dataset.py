from dataset_interface import DatasetInterface

import os
import cv2

class YoloDataset(DatasetInterface):

    
    def __init__(self, path):
        super().__init__(path)
        self.data = self.parse_from_path(path)
             

    def get_labels_path(self, ds_path):
        head, tail = os.path.split(ds_path.rstrip('/'))  # Remove trailing slash
        head, folder_before_last = os.path.split(head)

        # Define the new folder name
        labels_folder = "labels"

        # Create the new path by replacing the folder before the last one
        labels_path = os.path.join(head, labels_folder, tail)
        return labels_path

    
    def denormalize_yolo_bboxes(self, bboxes, image):

        height, width = image.shape[:2]
        #print('h x w', height, width)
        denormalized_bboxes = []
        for bbox in bboxes:
            cx = bbox[0] * width
            cy = bbox[1] * height
            obj_width = bbox[2] * width
            obj_height = bbox[3] * height
            xmin = cx - obj_width / 2
            ymin = cy - obj_height / 2
            xmax = xmin + obj_width
            ymax = ymin + obj_height
            denormalized_bboxes.append([xmin, ymin, xmax, ymax])

        return denormalized_bboxes
    
    # Recebe dataset e itera sobre ele, construindo um array de dict
    def parse_from_path(self, ds_path):
        # ds_path = /home/andrea/Dropbox/lsc/dengue/training-round-02/root-dir-to-upload/images/test/
        # /home/andrea/Dropbox/lsc/dengue/training-round-02/root-dir-to-upload/labels/test/000000000433.txt
        # /home/andrea/Dropbox/lsc/dengue/training-round-02/root-dir-to-upload/images/test/000000000433.jpg
        images_path = ds_path
        labels_path = self.get_labels_path(ds_path)

        arr = []
        # Iterate over all files in the folder
        for filename in os.listdir(images_path):
            # Check if the file is a .jpg image
            if filename.endswith(".jpg"):
                #print(filename)
                # Get the base filename (without extension) and create a new .txt filename
                base_filename = os.path.splitext(filename)[0]
                labels_filename = labels_path + '/' + base_filename + ".txt"
                bboxes = []
                labels = []
                with open(labels_filename, "r") as file:
                    for line in file:
                        # Split the line by spaces
                        fields = line.split()
                        
                        # The first field is the label
                        label = fields[0]
                        
                        # The remaining fields are the bounding box values 
                        bbox = [float(value) for value in fields[1:]]
                        bboxes.append(bbox)
                        labels.append(int(label))
                        #print(f"Label: {label}, Bounding Box: {bbox}")

                dict = {}
                dict['fname'] = filename
                dict['image'] = cv2.imread(ds_path + '/' + filename)
                dict['bboxes'] = [[int(n) for n in bbox] for bbox in self.denormalize_yolo_bboxes(bboxes, dict['image'])]
                dict['labels'] = labels
                arr.append(dict)

        return arr
        


