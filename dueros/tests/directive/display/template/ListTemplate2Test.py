#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/7/13

"""
    desc:pass
"""
import unittest
from dueros.directive.Display.template.ListTemplate2 import ListTemplate2
from dueros.directive.Display.template.ListTemplateItem import ListTemplateItem

class ListTemplate2Test(unittest.TestCase):
    '''
    ListTemplate2 单元测试
    '''
    
    def setUp(self):
        self.listTemplate2 = ListTemplate2()

    def testGetData(self):
        '''
        测试getData
        :return:
        '''

        self.listTemplate2.setBackGroundImage('http://back-img.com')

        listTemplateItem1 =  ListTemplateItem()
        listTemplateItem1.setImage('http://item-img1.com', '123', '345')
        listTemplateItem1.setPlainPrimaryText('Plain Primary Text')
        listTemplateItem1.setPlainSecondaryText('Plain Secondary Text')
        listTemplateItem1.setTertiaryText('Plain Tertiary Text')

        listTemplateItem1.data['token'] = 'token'

        listTemplateItem2 = ListTemplateItem()
        listTemplateItem2.setImage('http://item-img2.com', '12', '45')
        listTemplateItem2.setPlainPrimaryText('Plain Primary Text')
        listTemplateItem2.setPlainSecondaryText('Plain Secondary Text')
        listTemplateItem2.setTertiaryText('Plain Tertiary Text')

        listTemplateItem2.data['token'] = 'token'

        self.listTemplate2.addItem(listTemplateItem1)
        self.listTemplate2.addItem(listTemplateItem2)
        data = self.listTemplate2.getData()
        data['token'] = 'token'
        ret = {
            'type': 'ListTemplate2',
            'token': 'token',
            'backgroundImage': {
                'url': 'http://back-img.com'
            },
            'listItems': [
                {
                    'token': 'token',
                    'image': {
                        'url': 'http://item-img1.com',
                        'widthPixels': '123',
                        'heightPixels': '345'
                    },
                    'textContent': {
                        'primaryText': {
                            'type': 'PlainText',
                            'text': 'Plain Primary Text'
                        },
                        'secondaryText': {
                            'type': 'PlainText',
                            'text': 'Plain Secondary Text'
                        },
                        'tertiaryText': {
                            'type': 'PlainText',
                            'text': 'Plain Tertiary Text'
                        }
                    }
                },
                {
                    'token': 'token',
                    'image': {
                        'url': 'http://item-img2.com',
                        'widthPixels': '12',
                        'heightPixels': '45'
                    },
                    'textContent': {
                        'primaryText': {
                            'type': 'PlainText',
                            'text': 'Plain Primary Text'
                        },
                        'secondaryText': {
                            'type': 'PlainText',
                            'text': 'Plain Secondary Text'
                        },
                        'tertiaryText': {
                            'type': 'PlainText',
                            'text': 'Plain Tertiary Text'
                        }
                    }
                }
            ]
        }

        self.assertEqual(self.listTemplate2.getData(), ret)
    pass


if __name__ == '__main__':
    pass