from rest_framework import serializers
from api.models import Employees


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"
        