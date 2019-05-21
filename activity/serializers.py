from rest_framework import serializers
from . import models


class ActivitySerializers(serializers.ModelSerializer):
    activity_plan=serializers.CharField(source='activity_plan.activity_name')
    class Meta:
        # 关联数据表
        model = models.Activity
        # 确定需要序列化的数据
        # fields = ('number_of_college', 'activity_plan', 'content',)
        fields = '__all__'
        # def to_representation (self,instance):
        #     data=super().to_representation (instance)
        #     try:


class ActivityPlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ActivityPlan
        fields = '__all__'

class ActivitySummarySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ActivitySummary
        fields = '__all__'
