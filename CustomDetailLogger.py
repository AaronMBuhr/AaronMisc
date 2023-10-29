import logging

class CustomDetailLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)
        self.detail_level = 0

    def set_detail_level(self, level):
        if level > 0:
            self.setLevel(logging.DEBUG)
        self.detail_level = level

    def debug1(self, msg, *args, **kwargs):
        if self.detail_level >= 1:
            self.debug(msg, *args, **kwargs)

    def debug2(self, msg, *args, **kwargs):
        if self.detail_level >= 2:
            self.debug(msg, *args, **kwargs)

    def debug3(self, msg, *args, **kwargs):
        if self.detail_level >= 3:
            self.debug(msg, *args, **kwargs)

logging.setLoggerClass(CustomDetailLogger)
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
