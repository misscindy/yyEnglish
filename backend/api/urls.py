# coding=UTF-8

"""
Created on 5/25/18

@author: 'bingxinfan'
"""

from django.conf.urls import include, url

app_name = 'api'

urlpatterns = [
    url(r'accounts', include('api.accounts.urls')),
    url(r'api-auth',
        include('rest_framework.urls', namespace='rest_framework')),
]