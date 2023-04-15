#!usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
Filename         : views.py
Description      : 
Time             : 2023/03/31 17:23:14
Author           : AllenLuo
Version          : 1.0
'''

from ui_case.models import UI_test_detail
from ui_case.serializers import UITestUpdateSerializer, UITestDetailSerializer
from dvadmin.utils.viewset import CustomModelViewSet

class UITestModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    
    queryset = UI_test_detail.objects.all()
    serializer_class = UITestDetailSerializer
    update_serializer_class = UITestUpdateSerializer