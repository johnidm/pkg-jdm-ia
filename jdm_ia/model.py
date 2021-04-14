import os

def predict(model_name):
    ROOT_DIR = os.path.abspath(os.getcwd())
    model_path = os.path.join(ROOT_DIR, "models", model_name)
    dir_path = os.path.dirname(os.path.realpath(__file__))

    print('ROOT_DIR:      ', ROOT_DIR)
    print('model_path:    ', model_path)
    print('dir_path:      ', dir_path)

    with open(model_path) as f:
        return f.read()
