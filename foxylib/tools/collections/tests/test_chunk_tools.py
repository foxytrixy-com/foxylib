import logging
from unittest import TestCase

from foxylib.tools.log.foxylib_logger import FoxylibLogger
from foxylib.tools.collections.chunk_tool import ChunkTool


class TestChunkTool(TestCase):
    @classmethod
    def setUpClass(cls):
        FoxylibLogger.attach_stderr2loggers(logging.DEBUG)

    def test_01(self):

        x_iter = range(20)
        f_batch = lambda l:[min(l)]*len(l)
        f_cond = lambda x:x%2==0
        y_iter = ChunkTool.iter_batch_cond2processed(x_iter, f_batch, f_cond, (2,10))
        hyp = list(y_iter)
        ref = [0, 1, 0, 3, 4, 5, 4, 7, 8, 9, 8, 11, 12, 13, 12, 15, 16, 17, 16, 19]

        # pprint(hyp)

        self.assertEqual(hyp, ref)

    def test_02(self):
        x_iter = range(20)
        f_batch = lambda l:[min(l)]*len(l)
        f_cond = lambda x:x%2==0
        y_iter = ChunkTool.iter_batch_cond2processed(x_iter, f_batch, f_cond, (3,4))
        hyp = list(y_iter)
        ref = [0, 1, 0, 3, 4, 5, 4, 7, 8, 9, 8, 11, 12, 13, 12, 15, 16, 17, 16, 19]

        # pprint(hyp)

        self.assertEqual(hyp, ref)