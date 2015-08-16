__author__ = 'ysshiu'


class RegisterInfo(object):
    def __init__(self):
        self._name = 'unknown register'
        self._value = 0x00
        self._offset = 0x00
        self._address = 0x0000
        pass

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, offset):
        self._offset = offset

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def name(self):
        return self._name

    @address.setter
    def name(self, name):
        self._name = name
