#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/9/1

"""
    desc:pass
"""

from dueros.directive.Display.media.BaseMediaListItem import BaseMediaListItem


class AudioItem(BaseMediaListItem):
    """
    音频列表Item
    """

    def __init__(self, title, title_subtext1):
        BaseMediaListItem.__init__(self, title, title_subtext1)

    def set_music_video_tag(self, tag):
        """
        设置isMusicVideo
        :param tag:
        :return:
        """
        if isinstance(tag, bool):
            self.data['isMusicVideo'] = tag


if __name__ == '__main__':
    pass