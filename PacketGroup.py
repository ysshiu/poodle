__author__ = 'ysshiu'


class PacketGroup(object):
    def __init__(self):
        self._collection = []
        self._group_index = 0

    def add_register(self):
        self._collection.append(1)

    def add_registers(self, count):
        for i in xrange(0, count):
            self._collection.append(1)

    @property
    def group_index(self):
        return self._group_index

    @group_index.setter
    def group_index(self, value):
        self._group_index = value

