#!usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
Filename         : urls.py
Description      : 
Time             : 2023/03/16 21:32:32
Author           : AllenLuo
Version          : 1.0
'''

from rest_framework.routers import SimpleRouter

from api_case.views import ApiTestModelViewSet

router = SimpleRouter()
router.register("", ApiTestModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls