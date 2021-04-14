def predict():
    import os

    print('getcwd:      ', os.getcwd())
    print('__file__:    ', __file__)
    
    with open('./jdm_ia/models/generic.bin') as f:
        return f.read()