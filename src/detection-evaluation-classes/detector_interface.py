from abc import ABC, abstractmethod

class DetectorInterface(ABC):

    def __init__(self, path, model_size, img_size):
        pass
        # self.model_fn = None  # Placeholder for data, to be initialized by derived classes
        # self.model_size = model_size
        # self.img_size = img_size

    @abstractmethod
    def get_model_fn(self, path):
        pass

    @abstractmethod
    def get_predictions_for_dataset(self, ds):
        pass