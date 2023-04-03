from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel


class Api_test_detail(CoreModel):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    CaseNo = models.CharField(verbose_name=u'用例编号',max_length=128)  
    Summary = models.CharField(verbose_name=u'用例描述',max_length=128)  
    Domain = models.CharField(verbose_name=u'请求的域名端口',max_length=128) 
    InterfacePath = models.CharField(verbose_name=u'接口路径',max_length=128)  
    IsExecute = models.CharField(verbose_name=u'是否执行该用例',max_length=128)  
    Encode = models.CharField(verbose_name=u'是否需要加密处理',max_length=128)  
    MethodType = models.CharField(verbose_name=u'请求方法',max_length=128)  
    ParamsType = models.CharField(verbose_name=u'请求参数类型',max_length=128)  
    Params = models.TextField(verbose_name=u'请求参数', max_length=10000, null=True)  
    Sql = models.CharField(verbose_name=u'请求的sql语句',max_length=128, null=True, blank=True)  
    extract = models.CharField(verbose_name=u'要提取的变量',max_length=128, null=True, blank=True)  
    APIExpectResult = models.CharField(verbose_name=u'预期API接口返回的值',max_length=128)  
    SqlExpectResult = models.CharField(verbose_name=u'预期sql执行后返回的值',max_length=128, null=True, blank=True)  


    def __unicode__(self):
        '''
        以字符串的形式显示对象属性值
        '''
        return self.CaseNo
    class Meta:
        db_table = 'Api_test_detail' # 定义表的别名
        ordering = ['id']  # 按添加id排序