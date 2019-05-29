from rest_framework import serializers, validators
from . import models


class ActivityPlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ActivityPlan
        fields = '__all__'


# class ActivityPlanSerializers(serializers.Serializer):
#     activity_name=serializers.CharField()


class ActivitySerializers(serializers.ModelSerializer):
    # 下面两句，作用只能读不能改
    # activity_plan_name=serializers.CharField(source='activity_plan')
    # activity_plan_name=serializers.CharField(source='activity_plan.activity_name')
    # 需要重写update()
    # activity_plan = ActivityPlanSerializers()

    # def update(self, instance: models.Activity, validated_data):
    #     instance.activity_plan.activity_name = validated_data.get('activity_plan.activity_name', instance.activity_plan.activity_name)
    #     return instance

    class Meta:
        # 关联数据表
        model = models.Activity
        # 确定需要序列化的数据
        # fields = ('number_of_college', 'activity_plan', 'content',)
        fields = '__all__'
        # 遍历外键查询，也是只能读不能改
        depth = 2
        # 只读字段
        # read_only_fields =('activity_plan',)
        # 验证器
        # validators=[]

    # def validated_context(self,value):
    #     # if '测试'in value:
    #         raise serializers.ValidationError('有敏感字')
    #     return value
    def validate(self, attrs):
        '''
        重写validate函数
        校验反序列化的字段
        进行异常处理
        '''
        if '测试' in attrs['content']:
            raise serializers.ValidationError('有敏感字')
        return attrs


class ActivitySummarySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ActivitySummary
        fields = '__all__'
