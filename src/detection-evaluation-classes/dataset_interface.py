from abc import ABC, abstractmethod

class DatasetInterface(ABC):

    def __init__(self, path):
        self.data = []  # Placeholder for data, to be initialized by derived classes
        
    @abstractmethod
    def parse_from_path(self, path):
        pass
    
    
    def get_unique_classes(self):
        unique_classes = set()
        for entry in self.data:
            unique_classes.update(entry['labels']) 
        return list(unique_classes)

    def get_length(self):
        return sum(1 for _ in self.data)

    def get_data(self):
        return self.data
    

    def get_stats(self):

        unique_classes = self.get_unique_classes()

        stats = {}
        stats['image_count'] = self.get_length()
        stats['class_count'] = len(unique_classes)
        stats['classes'] = unique_classes
        
        all_truth = 0
        class_truth = [0] * len(unique_classes)

        for entry in self.data:
            truth_labels = entry['labels']
            all_truth += len(truth_labels)
            for i, class_id in enumerate(unique_classes):
                class_truth[i] += len([label for label in truth_labels if label == (class_id)])  

            #print(len(image_labels))
        stats['total_object_count'] = all_truth
        for i, class_id in enumerate(unique_classes):
            stats['class_' + str(i) + '_count'] = class_truth[i]
        
        return stats
    

    def get_groundtruth(self):
        truth_bboxes = []
        truth_labels = []
        fnames = []
        #sorted_array = sorted(self.data, key=lambda d: d['fname'], reverse=True)
        sorted_array = self.data
        for entry in sorted_array:
            fnames.append(entry['fname'])
            truth_bboxes.append(entry['bboxes'])
            truth_labels.append(entry['labels'])
    
        return fnames, truth_bboxes, truth_labels
    
    # Get groundtruths as dictionnaries of bboxes and labels, indexed by fname 
    def get_groundtruth_per_image(self):
        truth_bboxes = {}
        truth_labels = {}
        for entry in self.data:
            img_name = entry['fname']            
            truth_bboxes[img_name] = entry['bboxes'] 
            truth_labels[img_name] = entry['labels'] 

        return truth_bboxes, truth_labels


    def get_entry_by_fname(self, fname):
        for entry in self.data:
            if entry['fname'] == fname:
                return entry['image'], entry['bboxes'], entry['labels']
        return None