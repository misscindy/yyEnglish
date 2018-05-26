# coding=UTF-8

"""
Created on 5/25/18

@author: 'bingxinfan'
"""

import json
import sys

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import views, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


class FetchSomething(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, word):
        try:
            return Response('Good', status=status.HTTP_200_OK)
        except:
            # log_error(sys.exc_info())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

fetch_sth_view = FetchSomething.as_view()
