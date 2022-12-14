# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: xml_json_process.py
@create date: 2022/8/19 22:56
@description:
"""
import json

import xmltodict


def xml_to_json(xml_str):
    """
    xml转JSON
    :param xml_str:
    :return:
    """
    # parse是的xml解析器
    xml_parse = xmltodict.parse(xml_str)
    # json库dumps()是将dict转化成json格式,loads()是将json转化成dict格式。
    # dumps()方法的ident=1,格式化json
    json_str = json.dumps(xml_parse, indent=1)
    return json_str


def json_to_xml(json_str):
    """
    JSON转换为xml
    :param json_str:
    :return:
    """
    # xmltodict库的unparse()json转xml
    # 参数pretty 是格式化xml
    xml_str = xmltodict.unparse(json_str, pretty=1)
    return xml_str


def is_none(request_param):
    """
    过滤参数中为None的数据
    :param request_param:
    :return:
    """
    if isinstance(request_param, list):
        for index, a in enumerate(request_param):
            if isinstance(a, str):
                b = request_param.copy()
                if a is None:
                    del b[index]
            else:
                c = a.copy()
                for k, v in c.items():
                    if v is None:
                        del a[k]
                    if isinstance(v, list):
                        b = v.copy()
                        for index, a in enumerate(b):
                            if a is None:
                                del v[index]
    if isinstance(request_param, dict):
        c = request_param.copy()
        for k, v in c.items():
            if v is None:
                del request_param[k]
            if isinstance(v, list):
                b = v.copy()
                for index, a in enumerate(b):
                    if a is None:
                        del v[index]

    return request_param
