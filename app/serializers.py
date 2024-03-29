from rest_framework import serializers
from app.models import *






# serializers are dealing with querysets
# we are dealing json format of data for that we are converting our models into serializers 
# for that models we are creted modelserializer for each and everymodel classes
# it is used to serialize and deserialize the employee data in our database such as models


class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'


class WorkExperienceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkExperience
        fields='__all__'


class QualificationsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qualifications
        fields='__all__'


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'


class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

