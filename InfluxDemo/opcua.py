from time import sleep
from datetime import datetime
from collections import namedtuple


class PollOPCNode(object):
    """
    Define a tag to be polled
    Provide method to retreive values
    Storage of those values is not in scope for this Class
    """

    def __init__(self, node_string, client_obj, clean_string=None):
        self.node_str = node_string
        self.client = client_obj
        self.node = self.client.get_node(self.node_str)
        if clean_string is None:
            self.clean_string = self.node_str
        else:
            self.clean_string = clean_string

        # check if this is a valid node
        self._check_for_children()
        self._check_for_value()

    def _check_for_children(self):
        """
        Check if a node has children. It is assumped that if a node has children it should not be polled, thus throw an
        error.
        """
        if len(self.node.get_children()) > 0:
            raise ValueError('This Node is not a leaf node. Children of this node '
                             'are {}'.format(self.client.get_children()))

    def _check_for_value(self):
        """
        It is possible to define a tag that is not valid... check if there is a value associated with that tag.
        """
        self.node.get_value()

    def read_value(self, reads=1, _sleep=.1):
        """
        Read a value from an OPCUA tag

        :param reads: number of reads to perform
        :param _sleep: interval between reads
        :return:
        """
        values = []
        Result = namedtuple('Result', ['timestamp', 'fieldvalue', 'fieldname'])
        for count in range(reads):
            if reads > 1:
                sleep(_sleep)
            values.append(Result(datetime.now(), self.node.get_value(), self.clean_string))
        return values
