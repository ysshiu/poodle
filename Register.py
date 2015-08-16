__author__ = 'ysshiu'


import RegisterInfo
class Register(object):
    def __init__(self, register_info=None):
        self._info = register_info
        pass

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, register_info):
        self._info = register_info

    def read(self, bridge_controller):
        pass

    def write(self, bridge_controller):
        pass


def main():
    pass

if __name__ == '__main__':
    main()
