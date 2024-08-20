from abc import ABC, abstractmethod

class DetectorInterface(ABC):

    def __init__(self, path):
        self.model_fn = None  # Placeholder for data, to be initialized by derived classes

    @abstractmethod
    def get_model_fn(self, path):
        pass

    @abstractmethod
    def get_predictions_for_dataset(self, ds):
        pass