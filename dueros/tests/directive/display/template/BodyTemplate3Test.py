#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""
import unittest
from dueros.directive.Display.template.BodyTemplate3 import BodyTemplate3


class BodyTemplate3Test(unittest.TestCase):

    '''
    bodyTemplate测试
    '''

    def setUp(self):
        self.template = BodyTemplate3()
        self.template.setPlainContent('test')
        self.template.setImage('http://www.baidu.com')
        self.template.setBackGroundImage('http://www.baidu.com')
        self.template.setToken('0c71de96-15d2-4e79-b97e-e52cec25c254')

    def testGetData(self):
        '''
        测试getData
        :return:
        '''

        data = self.template.getData()
        ret = {
            'type': 'BodyTemplate3',
            'token': '0c71de96-15d2-4e79-b97e-e52cec25c254',
            'content': {
                'type': 'PlainText',
                'text': 'test'

            },
            'image':{
                'url':'http://www.baidu.com'
            },
            'backgroundImage': {
                'url': 'http://www.baidu.com'
            }
        }

        self.assertEqual(data, ret)
    pass


if __name__ == '__main__':
    pass