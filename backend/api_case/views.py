#!usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
Filename         : views.py
Description      : 
Time             : 2023/03/16 21:32:42
Author           : AllenLuo
Version          : 1.0
'''

# Create your views here.
from api_case.models import Api_test_detail
from api_case.serializers import ApiTestDetailCreateUpdateSerializer, ApiTestDetailSerializer
from dvadmin.utils.viewset import CustomModelViewSet
from loguru import logger

class ApiTestModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Api_test_detail.objects.all()
    serializer_class = ApiTestDetailSerializer
    create_serializer_class = ApiTestDetailCreateUpdateSerializer
    update_serializer_class = ApiTestDetailCreateUpdateSerializer
    filter_fields = ['Summary', 'CaseNo']
    search_fields = ['Summary']