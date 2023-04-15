#!usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
Filename         : serializers.py
Description      : 
Time             : 2023/03/31 17:21:10
Author           : AllenLuo
Version          : 1.0
'''


from ui_case.models import UI_test_detail
from dvadmin.utils.serializers import CustomModelSerializer
from application.settings import BASE_DIR
import os
import yaml
from rest_framework import serializers
from loguru import logger
from rest_framework.decorators import action

class UITestDetailSerializer(CustomModelSerializer):
    """
    序列化器
    """
    class Meta:
        model = UI_test_detail
        fields = "__all__"

    def to_representation(self, value):
        # 调用父类获取当前序列化数据，value代表每个对象实例ob, 额外输出指定字段内容
        data = super().to_representation(value)
        ui_case_path = os.path.join(BASE_DIR, "static", "autotest5", "test_demo2_case.yaml")
        with open(ui_case_path, "r", encoding="utf-8") as f:
            ui_case_content = yaml.safe_load(f)
        # 对序列化数据做修改，添加新的数据
        data['ui_case_content'] = ui_case_content
        return data

class UITestUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """
    def validate(self, data):
        yamlFileData = self.request.data['yamlFile']
        yaml.safe_load(yamlFileData) # 校验前端文件是否有格式问题
        ui_case_path = os.path.join(BASE_DIR, "static", "autotest5", "test_demo2_case22.yaml")
        with open(ui_case_path, "w+", encoding="utf-8", newline='') as f: # newline参数表示默认不做换行处理
            f.write(yamlFileData)
        return data

    class Meta:
        model = UI_test_detail
        fields = '__all__'