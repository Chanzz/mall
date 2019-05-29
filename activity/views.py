# from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import generics
import logging

import logging.handlers
logger = logging.getLogger(__name__)

LOG_FILE ='log/DEBUG_log'

# Create your views here.

# class ActivityViewSet(viewsets.ModelViewSet,
#                       # mixins.ListModelMixin,
#                       # mixins.RetrieveModelMixin,
#                       # mixins.CreateModelMixin,
#                       mixins.DestroyModelMixin,
#                       # mixins.UpdateModelMixin,
#                       ):
#     #查询所有信息
#     queryset = Activity.objects.all()
#     #序列化
#     serializer_class = ActivitySerializers

# class ActivityView(APIView):
#     def get(self,request):
#         '''查询所有'''
#         activity_list=Activity.objects.all()
#         act=ActivitySerializers(activity_list,many=True)
#         return Response(act.data)
#     def post(self,request):
#         '''添加'''
#         act=ActivitySerializers(data=request.data)
#         if act.is_valid():
#             act.save()
#             return Response(act.data)
#         return Response(act.errors)
#     def put(self,request,id):
#         '''修改'''
#         activity=Activity.objects.filter(pk=id).first()
#         act=ActivitySerializers(instance=activity,data=request.data)
#         if act.is_valid():
#             act.save()
#             return Response(act.data)
#         return Response(act.errors)
#     def delete(self,request,id):
#         '''删除'''
#         Activity.objects.filter(pk=id).delete()
#         return Response()

class ActivityView(
    # mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
    generics.ListCreateAPIView
):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializers


class ActivityDetailView(
    # mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin,generics.GenericAPIView
    generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializers
    def get(self, request, *args, **kwargs):
        handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)
        # fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
        # formatter = logging.Formatter(fmt)
        # handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        logger.info('[Success] ' + ip + ' has accessed in! ')
        return self.retrieve(request, *args, **kwargs)
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


class ActivityPlanView(generics.ListCreateAPIView):
    queryset = models.ActivityPlan.objects.all()
    serializer_class = serializers.ActivityPlanSerializers


class ActivityPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ActivityPlan.objects.all()
    serializer_class = serializers.ActivityPlanSerializers


class ActivitySummary(generics.ListCreateAPIView):
    queryset = models.ActivitySummary.objects.all()
    serializer_class = serializers.ActivitySummarySerializers


class ActivityDetailSummary(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ActivitySummary.objects.all()
    serializer_class = serializers.ActivitySummarySerializers
