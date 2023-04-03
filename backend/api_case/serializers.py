#!usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
Filename         : serializers.py
Description      : 
Time             : 2023/03/16 19:48:41
Author           : AllenLuo
Version          : 1.0
'''


from api_case.models import Api_test_detail
from dvadmin.utils.serializers import CustomModelSerializer


class ApiTestDetailSerializer(CustomModelSerializer):
    """
    序列化器
    """
    class Meta:
        model = Api_test_detail
        fields = "__all__"


class ApiTestDetailCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """
    class Meta:
        model = Api_test_detail
        fields = '__all__'