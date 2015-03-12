# -*- coding: utf-8 -*-
import tablib


class TabLibBaseRendererFactory(object):
    def __init__(self, info):
        """init"""

    def __call__(self, value, system):
        request = system.get('request')
        if request is not None:
            response = request.response
            ct = response.content_type
            if ct == response.default_content_type:
                response.content_type = self.content_type
        data = tablib.Dataset(*value.get('data', []),
                headers=value.get('headers', []),
                title=value.get('title'))
        return data


class XLSXRendererFactory(TabLibBaseRendererFactory):

    content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    def __call__(self, value, system):
        data = super(XLSXRendererFactory, self).__call__(value, system)
        return data.xlsx


class XLSRendererFactory(TabLibBaseRendererFactory):

    content_type = 'application/vnd.ms-excel'

    def __call__(self, value, system):
        data = super(XLSRendererFactory, self).__call__(value, system)
        return data.xls


class CSVRendererFactory(TabLibBaseRendererFactory):

    content_type = 'text/csv'

    def __call__(self, value, system):
        data = super(CSVRendererFactory, self).__call__(value, system)
        return data.csv


class HTMLRendererFactory(TabLibBaseRendererFactory):

    content_type = 'text/html'

    def __call__(self, value, system):
        data = super(HTMLRendererFactory, self).__call__(value, system)
        return data.html
