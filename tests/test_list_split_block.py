from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..list_split_block import ListSplit


class TestListSplit(NIOBlockTestCase):

    def test_process_signals(self):
        """Signals pass through block unmodified."""
        blk = ListSplit()
        self.configure_block(blk, {"list_att": "{{ $list }}"})
        blk.start()
        blk.process_signals([Signal({"list": [1, 2, 3]})])
        blk.stop()
        self.assert_num_signals_notified(3)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][-1].to_dict(),
            {"Attr": 3})
