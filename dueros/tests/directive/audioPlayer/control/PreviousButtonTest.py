#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
from dueros.directive.AudioPlayer.Control.PreviousButton import PreviousButton

class PlayPauseButtonTest(unittest.TestCase):

    def setUp(self):
        self.previousButton = PreviousButton()
        self.previousButton.setEnabled(False)
        self.previousButton.setSelected(True)

    def testGetData(self):

        ret = {
            'type': 'BUTTON',
            'name': 'PREVIOUS',
            'enabled': False,
            'selected': True
        }

        self.assertEqual(self.previousButton.getData(), ret)
    pass


if __name__ == '__main__':
    pass