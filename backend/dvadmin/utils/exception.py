#!usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
Filename         : exception.py
Description      : 
Time             : 2023/04/15 15:48:10
Author           : AllenLuo
Version          : 1.0
'''

import logging
import traceback
import yaml
from django.db.models import ProtectedError
from django.http import Http404
from rest_framework.exceptions import APIException as DRFAPIException, AuthenticationFailed
from rest_framework.views import set_rollback
from django.db import DatabaseError

from dvadmin.utils.json_response import ErrorResponse

logger = logging.getLogger(__name__)


def CustomExceptionHandler(ex, context):
    """
    统一异常拦截处理
    目的:(1)取消所有的500异常响应,统一响应为标准错误返回
        (2)准确显示错误信息
    :param ex:
    :param context:
    :return:
    """
    msg = ''
    code = 4000

    if isinstance(ex, AuthenticationFailed):
        code = 4001
        msg = ex.detail
    elif isinstance(ex,Http404):
        code = 40000
        msg = "接口地址不正确"
    elif isinstance(ex, DRFAPIException):
        code = 4002
        set_rollback()
        msg = ex.detail
        if isinstance(msg,dict):
            for k, v in msg.items():
                for i in v:
                    msg = "%s:%s" % (k, i)
    elif isinstance(ex, ProtectedError):
        set_rollback()
        msg = "删除失败:该条数据与其他数据有相关绑定"
    elif isinstance(ex, DatabaseError):
        code = 5000
        set_rollback()
        msg = "接口服务器异常,请联系管理员"
    elif isinstance(ex, yaml.YAMLError):
        code = 4003
        msg = '用例文件格式错误,请检查后提交'
    elif isinstance(ex, Exception):
        logger.error(traceback.format_exc())
        msg = str(ex)
    return ErrorResponse(msg=msg, code=code)
