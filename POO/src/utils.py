class ClassUtils:
    def __init__(self):
        self.obj = None

    def extract_class_attributes(self, _cls_obj):
        props = '\n'.join([f'{key}: {value}' for key, value in _cls_obj.__dict__.items()])
        return f'{_cls_obj.__class__}\n{props}'