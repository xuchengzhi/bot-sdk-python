#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""

import unittest
from dueros.directive.AudioPlayer.Control.ThumbsUpDownButton import ThumbsUpDownButton
from dueros.directive.AudioPlayer.Control.ThumbsUpDownButtonEnum import ThumbsUpDownButtonEnum
class ShowFavoriteListButtonTest(unittest.TestCase):

    def setUp(self):
        self.thumbsUpDownButton = ThumbsUpDownButton()
        self.thumbsUpDownButton.setSelectedValue(ThumbsUpDownButtonEnum.THUMBS_UP)

    def testGetData(self):

        ret = {
            'type': 'RADIO_BUTTON',
            'name': 'THUMBS_UP_DOWN',
            'selectedValue': 'THUMBS_UP'

        }

        self.assertEqual(self.thumbsUpDownButton.getData(), ret)
    pass


if __name__ == '__main__':
    pass