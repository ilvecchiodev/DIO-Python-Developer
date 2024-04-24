class ClassHelpers:

    def __init__(self):
        pass

    def extract_class_attributes(self,_class_obj):
        props = '\n'.join([f'{key}:{value}' for key, value in _class_obj.__dict__.items()])
        return f'{_class_obj.__class__.__name__}:\n{props}'