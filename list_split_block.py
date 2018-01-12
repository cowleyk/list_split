from nio.block.base import Block
from nio.properties import VersionProperty, Property, StringProperty
from nio.block.base import Signal

class ListSplit(Block):

    version = VersionProperty('0.1.0')
    list_att = Property(title="List", default=[])
    dict_att = StringProperty(title="Attribute Name", default="Attr")

    def process_signals(self, signals):
        for signal in signals:
            for elem in self.list_att(signal):
                self.notify_signals([Signal({self.dict_att(signal): elem})])
