__author__ = 'ysshiu'


import RegisterInfo
import PacketGroup

class PacketRegister(object):
    def __init__(self, register_info):
        self._info = register_info
        self._packet_group_clooection = []

    def add_register(self, group_index):
        for i in xrange(0, len(self._packet_group_clooection)):
            if self._packet_group_clooection[i].group_index == group_index:
                self._packet_group_clooection[i].append(1)

        new_packet_group = PacketGroup()
        new_packet_group.group_index = group_index
        new_packet_group.add_register()
        self._packet_group_clooection.append(new_packet_group)
