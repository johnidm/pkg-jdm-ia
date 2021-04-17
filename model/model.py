import os
import pickle
import numpy as np


class Model:

    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        model_path = os.path.join(Model.ROOT_DIR, "assets", "classifier.bin")
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, number):
        prediction = self.model.predict([number])
        return np.array(prediction).tolist()[0]
