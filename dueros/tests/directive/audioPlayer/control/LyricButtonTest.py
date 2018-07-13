#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
from dueros.directive.AudioPlayer.Control.LyricButton import LyricButton

class LyricButtonTest(unittest.TestCase):

    def setUp(self):
        self.lyricButton = LyricButton()
        self.lyricButton.setEnabled(False)
        self.lyricButton.setSelected(True)

    def testGetData(self):

        ret = {
            'type': 'BUTTON',
            'name': 'LYRIC',
            'enabled': False,
            'selected': True
        }

        self.assertEqual(self.lyricButton.getData(), ret)
    pass


if __name__ == '__main__':
    pass