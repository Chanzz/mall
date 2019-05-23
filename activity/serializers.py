from rest_framework import serializers
from . import models


class ActivityPlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ActivityPlan
        fields = '__all__'
# class ActivityPlanSerializers(serializers.Serializer):
#     activity_name=serializers.CharField()



class ActivitySerializers(serializers.ModelSerializer):
    # 下面两句，只能读不能改
    # activity_plan_name=serializers.CharField(source='activity_plan')
    # activity_plan_name=serializers.CharField(source='activity_plan.activity_name')
    # activity_plan_name=serializers.PrimaryKeyRelatedField(label='activity_plan_name',queryset=models.ActivityPlan.objects.all(),many=True)
    # activity_plan = ActivityPlanSerializers()
    #
    # def update(self, instance: models.Activity, validated_data):
    #     instance.activity_plan.activity_name = validated_data.get('activity_plan.activity_name', instance.activity_plan.activity_name)
    #     return instance

    class Meta:
        # 关联数据表
        model = models.Activity
        # 确定需要序列化的数据
        # fields = ('number_of_college', 'activity_plan', 'content',)
        fields = '__all__'
        depth = 1
        # read_only_fields =('activity_plan',)


class ActivitySummarySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ActivitySummary
        fields = '__all__'
