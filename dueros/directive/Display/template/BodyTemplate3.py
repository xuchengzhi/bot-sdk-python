#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/26

"""
BodyTemplate3模板
详见文档：https://dueros.baidu.com/didp/doc/dueros-bot-platform/dbp-custom/display-template_markdown#BodyTemplate3
"""

from dueros.directive.Display.template.TextImageTemplate import TextImageTemplate


class BodyTemplate3(TextImageTemplate):

    def __init__(self):
        TextImageTemplate.__init__(self, 'BodyTemplate3')


if __name__ == '__main__':
    pass