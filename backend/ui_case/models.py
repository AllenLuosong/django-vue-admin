#!usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
Filename         : models.py
Description      : 
Time             : 2023/03/31 17:21:21
Author           : AllenLuo
Version          : 1.0
'''

from django.db import models
import yaml
# Create your models here.
from dvadmin.utils.models import CoreModel


class UI_test_detail(CoreModel):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    ui_case_path = models.CharField(max_length=255, blank=True) # UI测试用例文件保存路径
    add_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)  # 设置时间格式，并自动更新
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)  # 设置时间格式，并自动更新
    

    def __unicode__(self):
        '''
        以字符串的形式显示对象属性值
        '''
        return self.ui_case_path
    
    class Meta:
        db_table = 'UI_test_detail' # 定义表的别名
        ordering = ['id']  # 按添加id排序