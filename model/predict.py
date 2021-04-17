import os
from .model import Model


def predict(num):

    model = Model()
    return model.predict(num)
