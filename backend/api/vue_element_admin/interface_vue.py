# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: interface_vue
@create date: 2022/8/20 21:25
@description:
"""

from flask import request
from flask_restful import Resource

from utils.status_code import response_code
from comm.comm_request_process import __REQ__
from comm.comm_response_process import response_result_process

from comm.comm_model_enum import modelEnum

from utils.log_config import logger


class InterfaceVue(Resource):
    def get(self):
        try:
            data = {
                'code': 20000,
                'data': {
                    'token': 'admin-token'
                }
            }
            return response_result_process(data)
        except Exception as e:
            logger.error(e)
            error_data = response_code.GET_DATA_FAIL
            return response_result_process(error_data)

    def post(self):
        xml = request.args.get('format')
        print(globals())
        try:
            request_data = __REQ__.request_process(request, xml, modelEnum.department.value)
            if isinstance(request_data, bool):
                request_data = response_code.REQUEST_PARAM_FORMAT_ERROR
                return response_result_process(request_data)
            if not request_data:
                data = response_code.REQUEST_PARAM_MISSED
                return response_result_process(data)
            fields = ['username', 'password']
            must = __REQ__.verify_all_param_must(request_data, fields)
            if must:
                return response_result_process(must)
            par_type = {'username': str, 'password': str}
            param_type = __REQ__.verify_all_param_type(request_data, par_type)
            if param_type:
                return response_result_process(param_type)
            data = {
                'code': 20000,
                'data': {
                    'token': 'admin-token'
                }
            }
            return response_result_process(data)
        except Exception as e:
            logger.error(e)
            error_data = response_code.TEST
            return response_result_process(error_data)
